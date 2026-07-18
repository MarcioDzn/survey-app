from sqlalchemy.exc import IntegrityError

from app.models import Survey


class SurveyRepository:
    def __init__(self, session):
        self.session = session

    def create(self, survey_data, code):
        survey_db = Survey(
            title=survey_data.title,
            code=code,
            description=survey_data.description,
            is_public=survey_data.is_public,
            is_active=survey_data.is_active,
        )

        self.session.add(survey_db)

        try:
            self.session.commit()
            self.session.refresh(survey_db)
            return survey_db

        except IntegrityError:
            self.session.rollback()
            raise Exception("Erro durante a criação do survey")

    def get_all(self):
        return self.session.query(Survey).all()

    def get_by_id(self, id):
        return self.session.query(Survey).filter(Survey.id == id).first()

    def get_by_code(self, code):
        return self.session.query(Survey).filter(Survey.code == code).first()

    def update(self, survey, survey_data):
        updated_data = {}
        for k, v in survey_data.dict(exclude_unset=True).items():
            if v is not None:
                updated_data[k] = v

        db_fields = set(c.name for c in survey.__table__.columns)

        for k, v in updated_data.items():
            if k in db_fields:
                setattr(survey, k, v)

        self.session.commit()
        self.session.refresh(survey)

        return survey

    def delete(self, survey):
        self.session.delete(survey)
        self.session.commit()
