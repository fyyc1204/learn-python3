import numpy as  np 


fangsans = np.array([[1.5,1.5,1.4],[100,1.0,1.0],[6.2,7.3,8.5],[6.2,7.3,8.5],[6.2,7.3,8.5],[1.2,7.3,3.5],[2.2,7.3,8.5],[2.2,7.3,8.5]]).T

print(fangsans)


print(np.array(fangsans[:,0]))

print(np.mean(np.array(fangsans[:,0]) /7 ))