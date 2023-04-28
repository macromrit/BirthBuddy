import openai

# hiding the confidential info from un-authorised users
with open("childcare/api_key.txt") as jammer:
    api_key_read = jammer.read()

parameters = {"temperature": .5, # more lower it is more creative it becomes -> value can range only from 0->1
              "max_tokens": 512, # 2^9
              "model": "text-davinci-003" # existing LLM on openai libray
              }

def renderPrompt(mom_dad_age: tuple, mom_dad_medical_ailments: tuple, collective_renumeration: float, country: str, married: bool, care_givers: bool, both_educated: bool, rapport_desc: str):
    # integrating api key
    openai.api_key = api_key_read
    
    prompt = F'''
    INSTRUCTION:
1) say yes or no in one word to have a baby after analyzing the given constraints given below
a)-> mom's and dad's age [ try to relate c section with moms age and medical ailment ]
b)-> mom's and dad's medical ailments [ if they have some suggest cure else appreciate them for being health ]
c)-> their yearly earnings combined in usd[ compare this with especially the country they live in for avg money needed to raise a child ]
d)-> their maritial status [ if married be a bit positive else be a bit negative in a subtle way ]
e)-> if they have caregivers good else explain why do they have to have one
f)-> country they live in [ use countries demographics, efficacy of pregnancy technologies in the country and infant moratlity rate for saying yes/no and the countries literacy rate aswell]
g)-> if they are educated give them potential problems they could have in future, if not educated explain the potential problems in a simpler way [ list out the problems they may face in having a child ]
h)-> Analyze their current rapport as a description will be given on it and say whats wrong and whats right in having a child in their live scenario

2) generate 8 paragraphs for the corresponding topics given above on your yes/no answer for the above question [ start and end paragraphs with # im going use it for regex processing]
template:
	Old's Gold but lets talk age
		a)#content#

	Gotta be healthy?
		b)#conten1t#

	Need to be a bit lucrative?
		c)#content#
	
	Goodness in exchanging rings
		d)#content#
	
	Necessity of an extra hand
		e)#content#
	
	Do you have to think about your Environment?
		f)#content#
	
	Children are cool, but lets talk the goodhead aches they give
		g)#content#
	
	Lifestyle and rapport
		h)#content#

EXAMPLE:

Based on the information provided, my recommendation is YES, you can have a baby! Let's break down the analysis for each constraint.

#Old's Gold but let's talk age
At 28 and 32, the parents are in a good age range for starting a family. While older mothers may have a higher risk for C-section, the age of the mother is not a concern at this point.

#Gotta be healthy?
There are no medical ailments to worry about for either parent, so that's great news! Keep up with regular check-ups and a healthy lifestyle to ensure a smooth pregnancy.

#Need to be a bit lucrative?
With an annual combined income of $100,000, the parents should be able to provide a comfortable life for their child. It's important to note that the cost of raising a child varies depending on where you live, but in general, it's doable with their income.

#Goodness in exchanging rings
Being married is a positive factor in starting a family. It provides a stable foundation for the child's upbringing and ensures a strong commitment from both parents.

#Necessity of an extra hand
Having caregivers in place is a great idea. Raising a child can be challenging, and having an extra hand can make a big difference in managing daily tasks.

#Do you have to think about your Environment?
The USA is a developed country with advanced medical technology, high literacy rates, and a low infant mortality rate. These factors make it a good environment for having a child. However, it's important to consider the impact on the environment and take steps to reduce waste and carbon footprint for the child's future.

#Children are cool, but let's talk the good headaches they give
Being educated means the parents are equipped to face any potential problems that may arise in raising a child. They may face challenges such as balancing work and family life, but with proper planning and support, they can overcome these obstacles.

#Lifestyle and rapport
A smooth lifestyle and respectful rapport between parents bodes well for starting a family. It's important to maintain open communication and work together to make decisions that are best for the child's well-being.

Overall, based on the given constraints, my recommendation is YES, you can have a baby! Wishing you all the best on your journey towards parenthood.


INPUT:

	a) mom's , dad's age: {mom_dad_age}
	b) medical ailments mom, dad: {mom_dad_medical_ailments}
	c) annual collective income's {collective_renumeration}
	d) Married: {"yes" if married else "no"}
	e) care-givers: {"yes" if care_givers else "no"}
	f) country: {country}
	g) Educated: {"yes" if both_educated else "no"}
	h) {rapport_desc}
	
	.............................................
    everything should be direct speech
	make a prediction on abv input by using the instruction given above [ reply in personal tone use and make it more humaly ]
    '''
    
    generative_model = openai.Completion.create(
        engine = parameters["model"],
        prompt = prompt,
        temperature = parameters["temperature"],
        max_tokens = parameters["max_tokens"],
    ) # method to contrive api response
    
    return list(map(lambda x: x[1].replace('\n', '<br>') if x[0] == 0 else x[1].replace('\n', '<br>').partition('<br>')[2], enumerate(generative_model.choices[0].text.strip().split('#'))))

if __name__=="__main__":
    # print(renderPrompt((45, 56), 
    #                 ('Aids', 'infertility'), 
    #                 2350000, 
    #                 "GERMANY", 
    #                 True, True, True, 
    #                 "Realizing the need of having a heir after forgetting about it citing corporate duties. would love to have a child now!!").__len__())
    pass