# Animação do Pêndulo Eletrostático e Lei de Coulomb com Manim

## Visão Geral

Esta animação, desenvolvida com a biblioteca Manim em Python, tem como objetivo ilustrar de forma didática o experimento do pêndulo eletrostático. Através dela, são explorados conceitos fundamentais da eletrostática, como carga elétrica, processos de eletrização (contato), força elétrica de repulsão, e a relação dessas grandezas, culminando na apresentação da Lei de Coulomb.

Este projeto foi desenvolvido como material de apoio para atividades do PIBID Física UFRJ, visando auxiliar na compreensão visual dos fenômenos eletrostáticos.


## Conteúdo da Animação

A animação é dividida nas seguintes etapas sequenciais:

1.  **Título:** Apresentação do tema "Pêndulo Eletrostático e a Lei de Coulomb".
2.  **Configuração do Pêndulo:**
    *   Introdução de um pêndulo simples, com um pivô, um fio e uma esfera (bob) representando a carga \(q_1\), inicialmente neutra.
3.  **Introdução da Carga Fixa:**
    *   Uma segunda esfera, representando uma carga fixa \(q_2\) (positiva), é aproximada do pêndulo.
4.  **Efeito da Repulsão (Eletrização por Contato):**
    *   A carga \(q_2\) toca a esfera do pêndulo \(q_1\).
    *   Ocorre a eletrização por contato, e \(q_1\) também adquire carga positiva (visualizada pela mudança de cor e um sinal "+").
    *   Como resultado, as duas cargas se repelem, e o pêndulo é defletido de sua posição de equilíbrio vertical.
5.  **Diagrama de Forças:**
    *   As forças atuantes na esfera do pêndulo em equilíbrio são mostradas:
        *   Força Peso (\(\vec{F}_g\))
        *   Força Elétrica (\(\vec{F}_e\))
        *   Tensão no fio (\(\vec{T}\))
    *   O diagrama é simplificado para focar na Força Elétrica (\(\vec{F}_e\)).
6.  **Demonstração do Efeito da Distância:**
    *   A distância \(r\) entre as cargas \(q_1\) e \(q_2\) é variada.
    *   Visualiza-se que a força elétrica (\(F_e\)) diminui com o aumento da distância e aumenta com a diminuição da distância.
    *   Um gráfico \(F_e \text{ vs. } r\) é exibido, mostrando a relação \(F_e \propto \frac{1}{r^2}\).
    *   Valores numéricos de \(r\), \(r^2\) e \(F_e\) (relativa) são mostrados dinamicamente.
7.  **Demonstração do Efeito do Produto das Cargas:**
    *   A intensidade relativa do produto das cargas (\(q_1 q_2\)) é variada (visualizada pelo tamanho dos sinais "+" nas esferas).
    *   Observa-se que a força elétrica (\(F_e\)) aumenta com o aumento do produto das cargas.
    *   A relação \(F_e \propto q_1 q_2\) é destacada.
    *   Valores numéricos do produto relativo das cargas e \(F_e\) (relativa) são mostrados.
8.  **Explicação da Lei de Coulomb:**
    *   Com base nas observações anteriores (\(F_e \propto q_1 q_2\) e \(F_e \propto \frac{1}{r^2}\)), a proporcionalidade combinada \(F_e \propto \frac{q_1 q_2}{r^2}\) é apresentada.
    *   Finalmente, a Lei de Coulomb é introduzida em sua forma completa: \(F_e = k \frac{|q_1 q_2|}{r^2}\), com uma breve menção à constante de Coulomb (\(k\)).

## Conceitos Chave Ilustrados

*   Carga Elétrica
*   Eletrização por Contato
*   Força Elétrica (Repulsão)
*   Diagrama de Corpo Livre (simplificado)
*   Dependência da Força Elétrica com a Distância (Lei do Inverso do Quadrado)
*   Dependência da Força Elétrica com o Produto das Cargas
*   Lei de Coulomb (introdução qualitativa e apresentação da fórmula)

## Pré-requisitos

Para executar esta animação, você precisará ter:

*   Python 3.7 ou superior
*   Manim Community (testado com v0.17.3, mas versões mais recentes devem funcionar)
    *   Instruções de instalação: [Manim Installation](https://docs.manim.community/en/stable/installation/uv.html)
*   NumPy (geralmente instalado como dependência do Manim)
*   Uma distribuição LaTeX completa (como MiKTeX para Windows, MacTeX para macOS, ou TeX Live para Linux)


## Contribuições e Melhorias

Sugestões de melhorias são bem-vindas!



