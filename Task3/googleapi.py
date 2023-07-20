import os
import numpy as np
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from config import GOOGLE_PROJECT_ID

""" Класс используется для хранение объектов dataset для последующего их взаимодействия с BigQuery API"""


class DatasetSchema:
    def __init__(self, id: str | int, labels: dict[str:str]):
        self.labels = labels
        self.id = id

    def __dict__(self):
        return {
            'datasetReference': {
                'datasetId': self.id
            },
            'labels': self.labels
        }





class BigQueryDSService:
    __NAME_API = 'bigquery'
    __VERSION_API = 'v2'
    __TOKEN_NAME = 'token.json'
    __SCOPES = ['https://www.googleapis.com/auth/bigquery']

    def __init__(self, project_id: str, cred: str):
        self.__project_id = project_id
        self.__read_token(cred)
        self.__service = build(self.__NAME_API, self.__VERSION_API, credentials=self.__creds)

    def __del__(self):
        self.__service.close()

    def get(self, dataset_id: str | int) -> dict:
        response = self.__service.datasets().get(projectId=self.__project_id, datasetId=dataset_id).execute()
        return response

    def list(self) -> dict:
        response = self.__service.datasets().list(projectId=self.__project_id).execute()
        return response

    def insert(self, ds: DatasetSchema) -> dict:
        response = self.__service.datasets().insert(projectId=self.__project_id, body=ds.__dict__()).execute()
        return response

    def delete(self, dataset_id: str | int):
        self.__service.datasets().delete(projectId=self.__project_id, datasetId=dataset_id).execute()

    def update(self, ds: DatasetSchema) -> dict:
        ds = ds.__dict__()
        body, dataset_id = ds['labels'], ds['datasetReference']['datasetId']
        response = self.__service.datasets().update(projectId=self.__project_id, datasetId=dataset_id,
                                                    body=body).execute()
        return response

    def __read_token(self, cred: str):
        creds = None
        if os.path.exists(self.__TOKEN_NAME):
            creds = Credentials.from_authorized_user_file(self.__TOKEN_NAME, self.__SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    cred, self.__SCOPES)
                creds = flow.run_local_server(port=0)
            with open(self.__TOKEN_NAME, 'w') as token:
                token.write(creds.to_json())
        self.__creds = creds


def main():
    bq_service = BigQueryDSService(GOOGLE_PROJECT_ID, 'cred.json')
    sin_val = np.sin(range(10))
    labels = {f'x_{i}': 'x' for i, x in enumerate(sin_val)}
    ds = DatasetSchema(1, labels)
    response = bq_service.insert(ds)
    print(response)
    response_2 = bq_service.list()
    print(response_2)


if __name__ == '__main__':
    main()
