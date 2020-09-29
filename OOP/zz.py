from gtts import gTTS as gt
import os

message = "Your have been hacked"
lan = "en"

obj =gt(text=message, lang=lan, slow=False)
obj.save('Virus.mp4')

for i in range(1):
    os.system('Virus.mp4')

#str ="PHURPASHERPA"
#for i in range(len(str)):
 #   for j in range(0,i+1):
  #      print(str[j],end="")
   # print()