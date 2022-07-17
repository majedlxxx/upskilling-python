# from employee import Department  => Circular import: because the employee file imports this file. / 2 files are importing each others
# a solution to a circular import is to conceal the import within a function / or an __name__ == "__main__" if statement



class Department:
    """
        name
        no_of_employees
        Link it with the employee constructors *
    """
    def __init__(self, name: str, no_of_employees: int= 0) -> None:
        from employee import Employee
        self.name = name
        self.no_of_employees = no_of_employees

        

if __name__ == "__main__":
    from employee import Employee