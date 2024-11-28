from datetime import datetime

class DateFormat:
    basis = "%Y-%m-%d"
    all = "%Y-%m-%d %H:%M:%S"

    @staticmethod
    def format(date:datetime) -> str:
        return date.strftime(DateFormat.basis)

    @staticmethod
    def parse(date:str, form:str=basis) -> datetime:
        return datetime.strptime(date, form)