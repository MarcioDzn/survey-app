from app.exceptions import NotFoundError
from app.utils import get_code


class SurveyService:
    def __init__(self, survey_repository, session):
        self.survey_repository = survey_repository
        self.session = session

    def create(self, survey_data):
        code = get_code()
        survey = self.survey_repository.get_by_code(code)

        # verifica se já existe uma survey com esse código
        while survey:
            code = get_code()
            survey = self.survey_repository.get_by_code(code)

        return self.survey_repository.create(survey_data, code)

    def get_all(self):
        return self.survey_repository.get_all()

    def get_by_id(self, id):
        survey = self.survey_repository.get_by_id(id)

        if not survey:
            raise NotFoundError("Survey não encontrado")

        return survey

    def get_by_code(self, code):
        survey = self.survey_repository.get_by_code(code)

        if not survey:
            raise NotFoundError("Survey não encontrado")

        return survey

    def update(self, id, survey_data):
        survey = self.survey_repository.get_by_id(id)

        if not survey:
            raise NotFoundError("Survey não encontrado")

        return self.survey_repository.update(survey, survey_data)

    def delete(self, id):
        survey = self.survey_repository.get_by_id(id)

        if not survey:
            raise NotFoundError("Survey não encontrado")

        return self.survey_repository.delete(survey)
