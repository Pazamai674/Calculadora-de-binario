# Calculadora-de-n-mero-bin-rio

# 🔍 String Parser - Extração de Nome e Documento (Slot Único)

Esta biblioteca/módulo foi desenvolvida para processar entradas de texto contendo dados compostos em um **slot único** de entrada e separar automaticamente as informações de **Nome** e **Documento** (CPF/CNPJ) utilizando Expressões Regulares (Regex).

O projeto conta com implementações funcionais para **C# (.NET 8)** e **Python 3**.

---

## 🚀 Funcionalidades

* **Processamento de Slot Único:** Recebe uma string bruta no formato `"Nome Sobrenome Documento"` sem a necessidade de múltiplos campos de entrada.
* **Validação por Regex:** Extrai o documento com ou sem pontuação (ex: `123.456.789-00` ou `12345678900`).
* **Tratamento de Exceções:** Retorna o texto original como nome caso nenhum padrão de documento válido seja identificado no final da string.
* **Suporte Multi-linguagem:** Exemplos prontos em C# e Python.

---

## 🛠️ Como Funciona

A lógica utiliza a expressão regular `^(.*?)\s*([\d\.\/-]+)$` para dividir a entrada em duas partes:

1. **Grupo 1 (Nome):** Captura todo o texto inicial até o último espaço antes dos números.
2. **Grupo 2 (Documento):** Captura a sequência final de dígitos contendo pontos, traços e barras.

---

## 💻 Exemplos de Uso

### **Python**
```python
slot_dados_usuario = "João da Silva 123.456.789-00"
resultado = processar_slot_unico(slot_dados_usuario)

print(resultado["nome"])       # Output: João da Silva
print(resultado["documento"])  # Output: 123.456.789-00
