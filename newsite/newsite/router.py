class Mydb2Router:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'mobilemarket':
            return 'mydb2'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'mobilemarket':
            return 'mydb2'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'mobilemarket' or obj2._meta.app_label == 'mobilemarket':
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'mobilemarket':
            return db == 'mydb2'
        elif db == 'mydb2':
            return False
        return None

class TVRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'mainsite':
            return 'mydb3'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'mainsite':
            return 'mydb3'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'mainsite' or obj2._meta.app_label == 'mainsite':
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'mainsite':
            return db == 'mydb3'
        elif db == 'mydb3':
            return False
        return None