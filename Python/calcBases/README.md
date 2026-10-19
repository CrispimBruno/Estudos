<div align="center">

<img src="imagensDoReadme/banner.png" width="70%" alt="Cris chibi estudando com fone azul"/>

# ⟦ CONVERSOR DE BASES ⟧

### `[ SISTEMA ]` 

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-EM%20DESENVOLVIMENTO-1f6feb?style=for-the-badge)
![Feito sem IA](https://img.shields.io/badge/FEITO%20SEM%20IA-0d1117?style=for-the-badge&logoColor=white)
![PUC Minas](https://img.shields.io/badge/PUC%20MINAS-ENG.%20SOFTWARE-0a0a23?style=for-the-badge)

*Binário, octal, decimal e hexadecimal. Tudo passando pela base 10.*

</div>

---

## ⚔️ `[ SOBRE O CONVERSOR / CALCULADORA ]`

Uma calculadora de bases numéricas feita **inteiramente em Python, sem IA no código**. uso de IA somente no read-me e nas imagens

A ideia é simples e em duas partes:

1. **Entrada → Decimal:** pega o número na base escolhida e transforma em base 10.
2. **Decimal → Saída:** pega esse decimal e transforma na base desejada.

Por enquanto tudo roda no **terminal**. O objetivo final é virar uma **calculadora com tela** de verdade.

---

## 🧭 `[ BASES DISPONÍVEIS ]`

| Código | Base | Dígitos válidos |
| :----: | :--- | :-------------- |
| `1` | Binário | `0` `1` |
| `2` | Octal | `0` a `7` |
| `3` | Decimal | `0` a `9` |
| `4` | Hexadecimal | `0` a `9` e `A` a `F` |
| `0` | Voltar | retorna à escolha da base |

---

## 🗺️ `[ FLUXO DO SISTEMA ]`

```text
   ┌─────────────────┐
   │  Escolher base  │  escolherBase1()
   │     inicial     │
   └────────┬────────┘
            ▼
   ┌─────────────────┐
   │ Digitar o número│  parte1()
   └────────┬────────┘
            ▼
   ┌─────────────────┐
   │ Verificar se é  │  verificadorBin / Oct / Dec / Hex
   │da base escolhida│
   └────────┬────────┘
            ▼
   ┌─────────────────┐
   │  Converter para │  binDec / octDec / decDec / hexDec
   │   decimal (10)  │
   └────────┬────────┘
            ▼
   ┌─────────────────┐
   │ Escolher base   │  parte2()
   │    de destino   │
   └────────┬────────┘
            ▼
   ┌─────────────────┐
   │Decimal → destino│  (em breve)
   └─────────────────┘
```

---

## 🧩 `[ ESTRUTURA DO CÓDIGO ]`

| Função | O que faz |
| :----- | :-------- |
| `escolherBase1()` | Menu para escolher a base inicial. Virou função para poder ser alterada depois |
| `parte1()` | Pede o número (digitar `0` volta ao menu) |
| `parte2()` | Menu da base correspondente ao segundo número |
| `chamadorDeFunção1()` | Função que chama outra função: define qual verificador e qual conversor usar |
| `verificadorBin / Oct / Dec / Hex` | Conferem se o número digitado pertence à base indicada |
| `binDec()` | Binário → decimal: cada dígito × 2^posição |

---

## 🚀 `[ COMO EXECUTAR ]`

```bash
# 1. clonar o repositório
git clone https://github.com/CrispimBruno/ESTUDOS.git

# 2. entrar na pasta
cd pyPlay/calcBases

# 3. rodar
python calcBases.py
```

---

## 📋 `[ MISSÕES ]`

**Concluídas**
- [x] Tela de boas-vindas e menu de escolha da base inicial
- [x] Estrutura das funções (uma por base, nomes resumidos)

**Em andamento** 🔥
- [ ] Verificadores de cada base
- [ ] Conversão para decimal: binário, octal, hexadecimal
- [ ] Segunda parte do fluxo (escolha da base de destino)

**Próximas**
- [ ] Conversão de decimal para a base desejada
- [ ] Tratamento de erros sem reiniciar o programa
- [ ] Interface gráfica: virar uma calculadora de verdade 🖥️


<div align="center">

**`[ Vai dar certo. ]`** 👑

*Feito com energético, fone e teimosia por **Crispim Bruno** · [GitHub](https://github.com/CrispimBruno)*

</div>
