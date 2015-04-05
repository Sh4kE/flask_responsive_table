import random

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()


class SwitchRandomState(Thread):

    def __init__(self, instances):
        self.instances = instances
        self.delay = 5
        super(SwitchRandomState, self).__init__()

    def switch_random_state(self):
        """
        Generate a random state every 5 seconds and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of random states
        while not thread_stop_event.isSet():
            instance_id = random.randint(1,self.instances)
            state = random.randint(0,1)
            socketio.emit('new_state', {'instance_id': instance_id}, namespace='/test')
            sleep(self.delay)

    def run(self):
        self.switch_random_state()
