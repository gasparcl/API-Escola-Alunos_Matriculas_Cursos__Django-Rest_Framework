from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, \
    MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosPorCursoSerializer

# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# Imports não serão utilizados para fins de consultas ao repositório

class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os alunos e alunas
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
   # authentication_classes = [BasicAuthentication]
   # permission_classes = [IsAuthenticated]
   # Autenticação não será utilizada para fins de consultas ao repositório




class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os cursos
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer



class MatriculasViewSet(viewsets.ModelViewSet):
    """
    Exibindo todas as matrículas
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer



class ListaMatriculasAluno(generics.ListAPIView):
    """
    Listando as matriculas de um aluno/a
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer



class ListaAlunosPorCurso(generics.ListAPIView):
    """
    Listando alunos matriculados por curso
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosPorCursoSerializer


