from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco
from projeto.models.enums.setores import Setores
from projeto.models.pessoaFisica import PessoaFisica
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

class Funcionario(PessoaFisica, ABC):
    @abstractmethod
    def __init__(self, id: int, nome: str, telefone: str, email: str, CPF: str, RG: str, matricula: str, setor: Setores, 
                 salario: int, endereco: Endereco, dataNascimento: str, genero: Generos, estadoCivil: EstadoCivil):
        super().__init__(id, nome, telefone, email, endereco, dataNascimento, genero, estadoCivil)
        self.CPF = self._verificar_CPF(CPF)
        self.RG = self._verificar_RG(RG)
        self.matricula = matricula
        self.setor = setor
        self.salario = salario


    def _verificar_CPF(self, CPF):
            if len(CPF) > 14:
                raise TypeError("CPF inválido")
            return CPF
        
    def _verificar_RG(self, RG):
            if len(RG) > 12:
                raise TypeError("RG inválido")
            return RG

    def __str__(self) -> str:
        return super().__str__()
    def __str__(self) -> str:
        return (f"\nCPF: {self.CPF}"
                f"\nRG: {self.RG}"
                f"\nNúmero de matricula: {self.matricula}"
                f"\nSetor: {self.setor}"
                f"\nSalário: {self.salario}")