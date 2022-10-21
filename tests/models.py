from django.db import models

class TestSet(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class TestSetAU(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class QAAU(models.Model):
    title = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    test = models.ForeignKey('TestSetAU', on_delete=models.PROTECT)

    def __str__(self):
        return self.correct_answer


class Questions_and_answers(models.Model):
    title = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    test = models.ForeignKey('TestSet', on_delete=models.PROTECT)

    def __str__(self):
        return self.correct_answer

# class ForAuthenticated(Questions_and_answers):
#
#     def __str__(self):
#         return self.correct_answer

# class Answers(models.Model):
#     correct_answer = models.CharField(max_length=200)
#     wrong_answer1 = models.CharField(max_length=200)
#     wrong_answer2 = models.CharField(max_length=200)
#     wrong_answer3 = models.CharField(max_length=200)
#     question = models.ForeignKey('Questions', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.correct_answer
#
