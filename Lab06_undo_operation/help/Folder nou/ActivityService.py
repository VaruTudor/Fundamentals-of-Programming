from ActivityRepository import*
from Exceptions import*
from PersonRepository import*
from PersonService import*
import random
class AService:
    def __init__(self,serv):
        self._personRepo=serv._repo
        self._repo=ARepo()
        self.init_list_of_activities()

    def init_list_of_activities(self):
        list_of_IDs=range(1000,9999)
        list_of_personIDs=[]
        people=self._personRepo.get_all()
        max_no_of_people=len(people)
        for i in people:
            list_of_personIDs.append(i._personID)
        list_of_days=range(1,32)
        list_of_months=range(1,13)
        list_of_years=range(2015,2026)
        list_of_hours=range(0,24)
        list_of_minutes=range(0,60)
        list_of_descriptions=['reading','watching movies','playing tennis','doing homework','eating','dancing','watching TV','concert','teambuilding']
        for i in range(10):
            chosen_id=str(random.choice(list_of_IDs))
            if self.validate_ID(chosen_id)=='valid':
                personIDs=self.generate_personIDs(list_of_personIDs,max_no_of_people)
                date=self.generate_valid_date(list_of_days,list_of_months,list_of_years)
                time=self.generate_valid_time(list_of_hours,list_of_minutes)
                if self.verify_overlapping_for_init(personIDs,date,time)==True:
                    description=random.choice(list_of_descriptions)
                    activity=Activity(chosen_id,personIDs,date,time,description)
                    self._repo.add(activity)
                else:
                    i=i-1
            else:
                i=i-1
        

    def validate_ID(self,activityID):
        result=self._repo.find_by_id(activityID)
        if result!=None:
            return 'invalid'
        return 'valid'

    def verify_overlapping_for_init(self,personIDs,date,time):
        for j in personIDs:
            result=self.verify_overlapping(j,date,time)
            if result=='Overlap':
                return False
        return True

    def generate_personIDs(self,list_of_personIDs,max_no_of_people):
        personIDs=[]
        chosen_no_of_people=random.choice(range(max_no_of_people+1))
        for i in range(chosen_no_of_people+1):
            chosed_personID=random.choice(list_of_personIDs)
            if chosed_personID not in personIDs:
                personIDs.append(chosed_personID)
            else:
                i=i-1
        return personIDs

    def generate_valid_date(self,list_of_days,list_of_months,list_of_years):
        valid_date=False
        while valid_date==False:
            year=str(random.choice(list_of_years))
            month=str(random.choice(list_of_months))
            day=str(random.choice(list_of_days))
            date=day+'.'+month+'.'+year
            try:
                result=self.validate_date(date)
                valid_date=True
            except BadDateError:
                valid_date=False
                continue
        return result

    def validate_date(self,value):
        if '.' not in value:
            raise BadDateError("Invalid date!")
        date=value.split('.')
        day=date[0]
        month=date[1]
        year=date[2]
        if len(month)==1:
                month='0'+month
        if len(day)==1:
            day='0'+day
        if day.isdigit()==False or month.isdigit()==False or year.isdigit()==False:
            raise BadDateError("Invalid date!")
        months_with_31=[1,3,5,7,8,10,12]
        if int(month) not in range(1,13):
            raise BadDateError("Invalid date!")
        elif month=='02' and int(year)%4==0 and int(day)>29:
            raise BadDateError("Invalid date!")
        elif month=='02' and not(int(year)%4==0) and int(day)>28:
            raise BadDateError("Invalid date!")
        elif int(month) not in months_with_31 and int(day)>30:
            raise BadDateError("Invalid date!")
        elif int(year) not in range(2015,2026):
            raise BadDateError("Invalid date!")
        return day+'.'+month+'.'+year
        

    def generate_valid_time(self,list_of_hours,list_of_minutes):
        hour=str(random.choice(list_of_hours))
        minute=str(random.choice(list_of_minutes))
        if len(hour)==1:
            hour='0'+hour
        if len(minute)==1:
            minute='0'+minute
        time=hour+':'+minute 
        return time       

    def get_all(self):
        return self._repo.get_all()


    def add_activity(self,activityID,list_of_personIDs,date,time,description):
        if self.validate_ID(activityID)=='invalid':
            raise BadIDError("This ID already exists!")
        formatted_date=self.validate_date(date)
        formatted_time=self.validate_time(time)
        if self.validate_personIDs(list_of_personIDs)==None and type(formatted_date)==str and type(formatted_time)==str:
            for j in list_of_personIDs:
                if self.verify_overlapping(j,date,time)=='Overlap':
                    raise OverlapError("The activities for "+j+" overlap!")
            activity=Activity(activityID,list_of_personIDs,formatted_date,formatted_time,description)
            self._repo.add(activity)

    def validate_personIDs(self,list_of_personIDs):
        people=self._personRepo.get_all()
        valid_personIDs=[]
        for i in people:
            valid_personIDs.append(i._personID)
        for i in list_of_personIDs:
            if i not in valid_personIDs:
                raise NonExistentID("The ID "+i+" is not in the planner.")
        return None

    def validate_time(self,time):
        if ':' not in time:
            raise BadTimeError("Invalid time!")
        time=time.split(':')
        hour=time[0]
        minute=time[1]
        if hour.isdigit()==False or minute.isdigit()==False:
            raise BadTimeError("Invalid time!")
        if int(hour) not in range(0,24) or int(minute) not in range(0,60):
            raise BadTimeError("Invalid time!")
        if len(hour)==1:
            hour='0'+hour
        if len(minute)==1:
            minute='0'+minute
        return hour+':'+minute

    def remove_by_id(self,activityID):
        element=self._repo.find_by_id(activityID)
        if element==None:
            raise NonExistentID("This ID does not exist in the list of activities!")
        self._repo.remove(element)


    def find_all_activities_for_a_person(self,personID):
        result=[]
        activities=self._repo.get_all()
        for activity in activities:
            for pID in activity._personID:
                if pID==personID:
                    result.append(activity)
                    break
        return result

    def verify_overlapping(self,personID,date,time):
        result=self.find_all_activities_for_a_person(personID)
        if result==[]:
            return None
        for i in result:
            if i.date==date and i.time==time:
                return  'Overlap'
        return None

    def update_activity(self,activityID,new_list_of_personIDs,new_date,new_time,new_description):
        element=self._repo.find_by_id(activityID)
        if element==None:
            raise NonExistentID("This ID does not exist in the list of people!")
        formatted_date=self.validate_date(new_date)
        formatted_time=self.validate_time(new_time)
        if self.validate_personIDs(new_list_of_personIDs)==None and type(formatted_date)==str and type(formatted_time)==str:
            for j in new_list_of_personIDs:
                if self.verify_overlapping_for_update(activityID,j,formatted_date,formatted_time)=='Overlap':
                    raise OverlapError("The activities for "+j+" overlap!")
            new_activity=Activity(activityID,new_list_of_personIDs,formatted_date,formatted_time,new_description)
            self._repo.update(element,new_activity)

    def verify_overlapping_for_update(self,activityID,personID,date,time):
        result=self.find_all_activities_for_a_person(personID)
        current_activity=self._repo.find_by_id(activityID)
        if result==[]:
            return None
        for i in result:
            if i!=current_activity and i.date==date and i.time==time:
                return  'Overlap'
        return None

        




