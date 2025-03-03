from abc import ABC, abstractmethod

#Base abstract class for all reports
class Report(ABC):
    '''Base class of reports'''
    def create(self):
        pass

#Class for generating a student Performance Report
class StudentPerformanceReport(Report):
    def create(self):
        from datetime import date
        import random
        
        current_date = date.today()
        
        report_id = random.randrange(0, 1000)
        
        data = f'Performance report up to date {current_date} ...'
        
        print(f'> Student Performance Report Generated with the id {report_id}')
        
        return {
            'report_date' : current_date,
            'report_id' : report_id,
            'data' : data
        }

#Class for generate a Subject Stadistics Report
class SubjectStadisticsReport(Report):
    def create(self):
        from datetime import date
        import random
        
        current_date = date.today()
        
        report_id = random.randrange(0, 1000)
        
        subjects = ['Maths', 'Physics', 'English']
        subject = random.choice(subjects)
        
        data = f'{subject} Stadistics up to date {current_date} ...'
        
        print(f'> {subject} Stadistics Report Generated with the id {report_id}')
        
        return {
            'report_date' : current_date,
            'report_id' : report_id,
            'data' : data
        }

#Class for generate as Programs Progress Report
class ProgramsProgressReport(Report):
    def create(self):
        from datetime import date
        import random
        
        current_date = date.today()
        
        report_id = random.randrange(0, 1000)
        
        data = f'Program Progress up to date {current_date} ...'
        
        print(f'> Program Progress Report Generated with the id {report_id}')
        
        return {
            'report_date' : current_date,
            'report_id' : report_id,
            'data' : data
        }

#Class for generate as Programs Progress Report
class RegistrantsListReport(Report):
    def create(self):
        from datetime import date
        import random
        
        current_date = date.today()
        
        report_id = random.randrange(0, 1000)
        
        subjects = ['Maths', 'Physics', 'English']
        subject = random.choice(subjects)
        
        data = f'List of registrants up to date {current_date} of {subject} subject...'
        
        print(f'> Resgistrants List Report Generated with the id {report_id}')
        
        return {
            'report_date' : current_date,
            'report_id' : report_id,
            'data' : data
        }

#Manager of the strategies
class ReportManager:
    def __init__(self, report_strategy, export_strategy):
        self.report_strategy = report_strategy
        self.export_strategy = export_strategy
    
    def set_report_strategy(self, report_strategy):
        self.report_strategy = report_strategy
    
    def set_export_strategy(self, export_strategy):
        self.export_strategy = export_strategy
    
    def create(self):
        return self.export_strategy.export(self.report_strategy.create())

class ReportExportType(ABC):
    def export(self):
        pass

class ReportToTXT(ReportExportType):
    def export(self, report):
        print(f'> Exporting {report} to txt...')

class ReportToPDF(ReportExportType):
    def export(self, report):
        print(f'> Exporting {report} to pdf...')

#We use a class in order to define the strategy to use
if __name__ == '__main__':
    try:
        context = ReportManager(StudentPerformanceReport(), ReportToTXT())
        
        print(context.create())
        
        context
    except Exception as e:
        print(f'!> An exception ocurred. Error: {e}')