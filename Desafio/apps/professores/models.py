from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class ProfessorModel(models.Model):
    
    #    A função VALIDADE a seguir efetua a validação do CPF, tanto formatação quanto dígito verificadores.
#    
#   PARA CRITERIO DE TESTE, INDICO O https://www.4devs.com.br/gerador_de_cpf
#   PARA GERAR CPF VALIDOS E INVALIDOS PARA TESTE
#
#    Parâmetros:
#        cpf (str): CPF a ser validado
#
#   Retorno:
#        bool:
#            - Falso, quando o CPF não possuir o formato 99999999999;
#            - Falso, quando o CPF não possuir 11 caracteres numéricos;
#            - Falso, quando os dígitos verificadores forem inválidos;
#            - Verdadeiro, caso contrário.
#
#    Exemplos:
#
#    Se validate('57261914045')
#        True
#    Se validate('52998224725')
#        False
#    Se validate('11111111111')
#        False

    def validate(value: str) -> bool:

        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in value if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            raise ValidationError(
                _('Um CPF VÁLIDO com 11 números. DIGITE APENAS OS NÚMERO.'), code='invalid_cpf')


        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            raise ValidationError(
                _('Um CPF VÁLIDO com 11 números. DIGITE APENAS OS NÚMERO.'), code='invalid_cpf')

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            raise ValidationError(
                _('Um CPF VÁLIDO com 11 números. DIGITE APENAS OS NÚMERO.'), code='invalid_cpf')

        return True
    
    FORMACAO = (
        ( 'G', 'Graduação'),
        ( 'M', 'Mestrado'),
        ( 'D', 'Doutorado'),
    )
    
    # Declaração das colunas da tabela do banco de dados de Professores
    
    id = models.AutoField(primary_key=True, auto_created=True)
    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, validators=[validate], blank=False, null=False, unique=True)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    formacao = models.CharField(max_length=1, choices=FORMACAO, blank=False, null=False, default='G')
    
    def __str__(self) -> str:
        return self.nome

