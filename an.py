# note: 3 distinct classes of neurons in biology - sensory, motor, interneurons
# another possible class- neural circut:a group of connected neurons



class Neuron():                                                                          # can make a parent class from which sensory,motor,inter can inherit?
    def __init__(self, num_axon, num_dendrite, membrane_potential, input_voltage):

        #-----properties-----
        #self.num_axn = num_axon                                                   # output transmitter          make Axon class?
        #self.num_den = num_dendrite                                               # input receiver   
        self.threshold_potential = -50                                            # membrane potential level required to trigger action potential
        self.resting_membrane_potential = -70
        self.membrane_potential = self.resting_membrane_potential                 # voltage in cell, increased or decreased by sodium and potassium ions, initialized to resting potential value
        self.input_vlt = input_voltage
        #self.connections = connections[]                                         # has a list containing names of other neurons its connected with
        # maybe 2 lists, output_connections and input_conns?

    #------functions------
    def action_potential(self):                                                           # (aka nerve impulse, spike)
        if self.membrane_potential >= self.threshold_potential:
            #send 'ping' to each neuron in output_conn list
            print('firing')
        else:
            print('not firing')

'''
#----misc----
while membrane_potential > resting_membrane_potential:                  # simulates cell membrane potential returning to normal level over time
    pass
    #membrane_potential -= 1
    #wait 1 sec

if received_input:
    pass
     #membrane_potential += 1

'''



n = Neuron(3,6,-70,50)
print(n.membrane_potential)

'''

class SensoryNeuron():
    Neuron.super()

    received_external_stimulus
    
    
class MotorNeuron
    Neuron.super()

    outputs_signal


'''