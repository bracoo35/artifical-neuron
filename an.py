#note: 3 distinct classes of neurons in biology - sensory, motor, interneurons
#another possible class- neural circut:a group of connected neurons



class Neuron():                                           # can make a parent class from which sensory,motor,inter can inherit?
    def __init__(self, num_axon, num_dendrite, membrane_potential):

        #-----properties-----
        self.num_axn = num_axon                             #output/transmitter          make Axon class?
        self.num_den = num_dendrite                           #input/receiver   
        self.threshold_potential = -50                   #membrane potential level required to trigger action potential)
        self.membrane_potential = membrane_potential                   #voltage in cell, increased or decreased by sodium and potassium ions)
        self.resting_membrane_potential = -70

    #------functions------
    def action_potential(self):                         # (aka nerve impulse, spike)
        if self.membrane_potential >= self.threshold_potential:
            print('firing')
        else:
            print('not firing')



n = Neuron(3,6,-80)
n.action_potential()



