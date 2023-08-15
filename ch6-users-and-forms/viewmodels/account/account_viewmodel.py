from data.user import User
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user = User("Miracle", "micool123@gmail.com", "9hsdhhsy74s")
