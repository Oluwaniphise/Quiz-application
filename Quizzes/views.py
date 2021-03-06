from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Question, Choice, Course, UserChoice
from django.core.paginator import Paginator, EmptyPage

# for the courses list


def courses_list(request):
    all_course = Course.objects.all()
    context = {
        'courses': all_course
    }
    return render(request, 'Quiz/course-list.html', context)


# for the courses detail
def course_detail(request, course):
    current_user = request.user
    course = Course.objects.get(title=course)
    context = {
        'user': current_user, 'course': course
    }
    return render(request, 'Quiz/course-detail.html', context)


# for the courses quiz
def course_quiz(request, course_title):
    """
    site_url/{{course}}/questions/
    Get the current user, the questions and choices
    Render them in context
    """
    current_user = request.user
    # get the course from the course_id
    course = Course.objects.get(title=course_title)
    questions = course.question_set.all().order_by(
        'id')  # get the questions through course

    # for the page pagination
    paginator = Paginator(questions, 1)
    page_num = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_num)
    except EmptyPage:
        page_obj = paginator.page(1)

    # for the user selection
    try:
        # find a way to get the current question from the pagination's page
        # object list contains the objects in the page
        question = page_obj.object_list.get()
        user_choice = question.choice_set.get(pk=request.POST['choice'])
        print(user_choice)
        # save the user's choice
        is_correct = Choice.objects.get(
            question=question, choice_text=user_choice, course=course).answer
        save_user_choice = UserChoice(
            user=request.user,
            user_choice=user_choice,
            is_correct=is_correct,
            course=course
        )
        save_user_choice.save()
        # proceed to the next question
        page_num = page_obj.next_page_number
        # page_obj = paginator.page(page_num)
    except (KeyError, Choice.DoesNotExist):
        # Display the question form again
        # this may be buggy as it's not tested.
        return render(request, 'Quiz/course-quiz.html', {
            'user': current_user, 'course': course,
            'questions': page_obj, 'paginator': paginator,
            'page_num': page_num,
            'error_message': "Try selecting an option!",
        })

    context = {
        'user': current_user, 'course': course,
        'questions': page_obj, 'paginator': paginator,
        'page_num': page_num
    }
    return render(request, 'Quiz/course-quiz.html', context)
