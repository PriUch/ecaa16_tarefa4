import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
#import soma

rospy.init_node('no_matricula')

soma_string = String()

def sub_matriculaCallBack(msg):
    global resultado_soma
    resultado_soma = msg

def timerCallBack(event):
    msg = String()
    msg.data = 'Matricula: 2016000168'
    pub_matricula.publish(msg)
    print('Soma da matricula = '+resultado_soma.data)
    
pub_matricula = rospy.Publisher('/no_matriucla/matricula', String, queue_size=1)
sub_matricula = rospy.Subscriber('/no_soma/soma', String, sub_matriculaCallBack)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin() 