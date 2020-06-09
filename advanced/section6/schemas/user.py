from ma import ma
from marshmallow import pre_dump
from models.user import UserModel
from schemas.confirmation import ConfirmationSchema


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_only = ('password',)
        dump_only = ('id', 'confirmation')
        include_relationships = True
        load_instance = True

    @pre_dump
    def _pre_dump(self, user: UserModel, many, **kwargs):
        user.confirmation = [user.most_recent_confirmation]
        return user
