'''
                            M O D E L   M A N A G E R
                        - - - - - - - - - - - - - - - - - 

=> At Manager is the interface through which database query operations are provided to Django MOdels.
=> At least one Manager exists for each model.
=> Model Manager is used to interact with database.
=> By default, Django adds a Manager with the name objects to evry Django model class. e.g: -  User.objects.all (objects here is the model manager for User Model).

'''




'''
                            C H A N G E   M A N A G E R     N A M E
                        - - - - - - - - - - - - - - - - - - - - - - - -

=> By defaults, Django adds a Manager with the name objects to every Django model class. However, if you want to use objects as a field name, or if you want to use a name other than objects for the Manager, you can rename it on a per-model basis.
=> To rename the Manager for a given class, define a class attribute of type models.Manger() on that model.
    e.g :- class Student(models.Model):
                id = uuid(UUID)
                topic = models.CharField(max_length = 70)
                manager_name = models.Manager()    # by default it is objects = models.Manager()
           $ QUERY => student_data = Student.manager_name.all()
'''



'''
                            C U S T O M     M O D E L    M A N A G E R
                        - - - - - - - - - - - - - - - - - - - - - - - - - -

=> You can use a custom Manager in a particular model by extending the base Manager class and instantiating you custom Manager in your Model.

=> A custom Manager method can return anything you want. It does'nt have to return a QuerySet.
    > to modify the initial QuerySet the Manager returns
    > to add extra Manager methods

=> MODIFY INITAL QUERYSET :-  ! A Manager's base QuerySet returns all objects in the system. You can overide a Manager's base Queryset by overriding the Manager.get_queryset() method.get_queryset() should return a QuerySet with the properties you require.
                              ! Default :- objects.all()

                              example :-
                                  SETP 1:  { -- WRITE MODEL MANAGER -- }
                                    class CustomManager(models.Manager):
                                        def get_queryset(self):   # overriding Built-in method called when we call all()
                                            return super().get_queryset().order_by('name')  # now the base queryset is overrided with base + ordered by name = all.order_by('name')
                        

                                  STEP 2: { -- ASSOCIATE MODEL MANAGER -- }
                                    class Student(models.Model):
                                        name = models.CharField(max_length = 100)

                                        objects = models.Manager() #default --> change it or keep it, ^^^ To keep it use have to write in the model.
                                        vidhyarthi = models.CustomManager() --> replace objects by this or append it 

                                    # Now, if we keep multiple Manager for the Student than whichever manager is used during querying resulting queryset will be according to that.
                                            !! students = Student.objects.all() will return  all the student objects
                                            !! students = Student.vidhyarthi.all() will return  all the student objects order by name
                                     
'''         