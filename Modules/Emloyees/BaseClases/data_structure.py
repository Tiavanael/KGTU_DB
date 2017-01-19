

class Structure(object):
    """
    Данный класс хранит структуру данных
    для работы с "Сотрудниками" (Employees).

    Property:
             id: <int> : номер сотрудника
            fio: <str> : ФИО
         salary: <str> : зарплата
     department: <str> : отдел
    """


    def __init__(
            self,
            fio=None,
            salary=None,
            department=None,
            post=None
    ):

        self.__init_Attributes()
        self.__init_Parameters(
            fio=fio,
            salary=salary,
            department=department,
            post=post
        )




    # inits
    def __init_Attributes(self):
        super(Structure, self).__init__()
        self.__fio = ''
        self.__salary = 0
        self.__post = ''
        self.__department = ''

    def __init_Parameters(self, fio, salary, department, post):
        if fio: self.setFIO(fio)
        if salary: self.setSalary(salary)
        if department: self.setDepartment(department)
        if post: self.setPost(post)


    

    @property
    def asFieldsForRecord(self):
        return [
            self.__fio,
            self.__salary,
            self.__department,
            self.__post
        ]
    
    @property
    def FIO(self):
        try:
            return self.__fio
        except:
            return None

    @property
    def salary(self):
        try:
            return self.__salary
        except:
            return None

    @property
    def department(self):
        try:
            return self.__department
        except:
            return None

    @property
    def post(self):
        return self.__post



    # METHODS
    def setFIO(self, fio=''):
        fio = str(fio)
        self.__fio = fio

    def setSalary(self, salary=0):
        self.__salary = int(salary)

    def setDepartment(self, department):
        self.__department = str(department)

    def setPost(self, post):
        self.__post = post