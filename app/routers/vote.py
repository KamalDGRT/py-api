from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from .. import schemas, database, models, oauth2

router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
def vote(
    vote: schemas.Vote,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user)
):

    # First check if there is a post where we can actually vote
    post = db.query(models.Post).filter(
        models.Post.id == vote.post_id
    ).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {vote.post_id} does not exist"
        )

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id,
        models.Vote.user_id == current_user.id
    )

    found_vote = vote_query.first()

    if (vote.dir == 1):
        # checking if already voted
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"user {current_user.id} has alredy voted on post {vote.post_id}"
            )

        # if not voted, then adding a new vote
        new_vote = models.Vote(
            post_id=vote.post_id,
            user_id=current_user.id
        )
        db.add(new_vote)
        db.commit()
        return {
            "message": "Successfully added vote!"
        }
    else:
        # if user provided a dir as 0, or that he wants to delete a vote,
        #  then check if the vote exists. that we have done above, so,
        #  we are just using it here. if not found, raise exception.
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vote does not exist"
            )

        # if we did find a vote, we have to delete it
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {
            "message": "successfully deleted vote"
        }
