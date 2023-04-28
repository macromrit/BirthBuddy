from django.shortcuts import render
from childcare import llm_helper_function
# Create your views here.
def homeForms(request):
    return render(request, 'childcare/home.html', {"error" : None})


def dispViews(request):
    desc = request.GET.get('rapport')
    
    if not desc:
        return render(request, 'childcare/home.html', {"error": "Its cool to describe your mutual rapport, Don't skip it!!!"})

    mom_dad_age= request.GET.get('agemom'), request.GET.get('agedad')
    
    medical_ailments_mom_dad = request.GET.get('medicalailmentsmom'), request.GET.get('medicalailmentsdad')
    
    country = request.GET.get('country')
    
    married = request.GET.get('marriedornot')
    caretakers = request.GET.get('caretakers')
    
    renumeration = request.GET.get('renumeration')
    degree = request.GET.get('gotdegree')
    
    solution_list = llm_helper_function.renderPrompt(mom_dad_age, medical_ailments_mom_dad, renumeration, country, married, caretakers, degree, desc)
    
    return render(request, 'childcare/dispViews.html', 
        {"part1": solution_list[0], 
         "part2": solution_list[1],
         "part3": solution_list[2],
         "part4": solution_list[3],
         "part5": solution_list[4],
         "part6": solution_list[5],
         "part7": solution_list[6],
         "part8": solution_list[7],
         "part9": solution_list[8],}
        )