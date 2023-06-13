#pip install googletrans

from googletrans import Translator
translater = Translator()
my_text= translater.translate("stick to the truth and the truth will save you back", dest="hi")
print(my_text.text)
# సత్యానికి కట్టుబడి ఉండండి మరియు నిజం మిమ్మల్ని తిరిగి రక్షిస్తుంది