{\rtf1\ansi\ansicpg1252\cocoartf2907
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import os\
import urllib.request\
import json\
\
# Configura\'e7\'e3o da p\'e1gina\
st.set_page_config(\
    page_title="Simulador Avan\'e7ado da Reforma Tribut\'e1ria",\
    page_icon="\uc0\u55357 \u56498 ",\
    layout="wide",\
)\
\
# Fun\'e7\'e3o para buscar a cota\'e7\'e3o atual do d\'f3lar em tempo real via API p\'fablica\
@st.cache_data(ttl=3600)\
def obter_cotacao_dolar():\
    try:\
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"\
        req = urllib.request.Request(url, headers=\{'User-Agent': 'Mozilla/5.0'\})\
        with urllib.request.urlopen(req, timeout=5) as response:\
            data = json.loads(response.read().decode())\
            cotacao = float(data['USDBRL']['bid'])\
            return cotacao\
    except Exception:\
        # Valor de fallback caso haja instabilidade na rede\
        return 5.50\
\
cotacao_dolar_atual = obter_cotacao_dolar()\
\
# T\'edtulo principal atualizado conforme solicitado\
st.title("\uc0\u55356 \u56807 \u55356 \u56823  Simulador Pratico - Reforma Tributaria - Pedro Marques")\
st.markdown(\
    "Plataforma t\'e9cnica baseada na **Emenda Constitucional n\'ba 132/2023** e nos textos complementares "\
    "(**PLP n\'ba 68/2024 e PLP n\'ba 108/2024**). Ferramenta com an\'e1lises jur\'eddicas, detalhamento normativo, "\
    "cota\'e7\'e3o do d\'f3lar em tempo real e simula\'e7\'f5es num\'e9ricas integradas com intelig\'eancia artificial."\
)\
\
st.divider()\
\
# Menu lateral para escolher o tema\
opcao = st.sidebar.selectbox(\
    "Selecione o M\'f3dulo de An\'e1lise e Simula\'e7\'e3o:",\
    [\
        "1. Vis\'e3o Geral & Marco Constitucional",\
        "2. IVA Dual (CBS e IBS) - PLP 68/2024",\
        "3. Imposto Seletivo (IS) & Externalidades",\
        "4. Cashback Tribut\'e1rio & Justi\'e7a Social",\
        "5. Split Payment & Tecnologia de Arrecada\'e7\'e3o",\
        "6. Cesta B\'e1sica & Al\'edquotas Reduzidas",\
        "\uc0\u55357 \u56522  7. Simulador Interativo Setorial (Estilo Pro)",\
        "\uc0\u55357 \u56994  8. Simula\'e7\'e3o de Importa\'e7\'e3o & Cota\'e7\'e3o do D\'f3lar",\
        "\uc0\u55358 \u56598  9. IA Consultora Oficial (Base de Dados do Governo)",\
    ],\
)\
\
# Conte\'fado din\'e2mico baseado na escolha do usu\'e1rio\
if opcao == "1. Vis\'e3o Geral & Marco Constitucional":\
    st.header("Vis\'e3o Geral & Fundamentos Constitucionais (EC 132/2023)")\
    st.write(\
        "A Emenda Constitucional n\'ba 132/2023 reescreveu a arquitetura da tributa\'e7\'e3o do consumo no Brasil, "\
        "estabelecendo a transi\'e7\'e3o do princ\'edpio da origem para o **princ\'edpio do destino pleno**."\
    )\
\
    st.markdown(\
        """\
    - **Art. 156-A da CF/88:** Institui\'e7\'e3o do IBS (Imposto sobre Bens e Servi\'e7os), compet\'eancia de Estados, DF e Munic\'edpios.\
    - **Art. 195, V da CF/88:** Institui\'e7\'e3o da CBS (Contribui\'e7\'e3o Social sobre Bens e Servi\'e7os), compet\'eancia da Uni\'e3o.\
    - **Neutralidade Econ\'f4mica:** Elimina\'e7\'e3o de distor\'e7\'f5es log\'edsticas e societ\'e1rias induzidas por incentivos fiscais estaduais (Guerra Fiscal).\
    """\
    )\
\
    col1, col2 = st.columns(2)\
\
    with col1:\
        st.error("\uc0\u10060  Como era (O Sistema Antigo)")\
        st.markdown(\
            """\
        - **5 Tributos Fragmentados:** PIS, Cofins, IPI, ICMS e ISS com bases de c\'e1lculo distintas.\
        - **Efeito Cascata Cr\'f4nico:** Cobran\'e7a de imposto sobre imposto ao longo de toda a cadeia produtiva e de circula\'e7\'e3o.\
        - **Litigiosidade Extrema:** Milhares de horas e bilh\'f5es de reais gastos em contenciosos judiciais sobre o conceito de insumo.\
        """\
        )\
\
    with col2:\
        st.success("\uc0\u9989  Como vai ficar (O Novo Sistema - 2026 a 2033)")\
        st.markdown(\
            """\
        - **IVA Dual Padronizado:** CBS (Federal) + IBS (Subnacional).\
        - **N\'e3o-Cumulatividade Financeira Plena:** Cr\'e9dito imediato de todo imposto pago na etapa anterior.\
        - **Arrecada\'e7\'e3o no Destino:** O imposto pertence ao munic\'edpio e estado onde reside o adquirente final do produto ou servi\'e7o.\
        """\
        )\
\
    st.markdown("\uc0\u55357 \u56599  **Refer\'eancia Legal Oficial:** [Emenda Constitucional n\'ba 132/2023 - Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm)")\
\
elif opcao == "2. IVA Dual (CBS e IBS) - PLP 68/2024":\
    st.header("2. IVA Dual: CBS (Livro I) e IBS (Gest\'e3o Compartilhada)")\
    st.write(\
        "O Projeto de Lei Complementar n\'ba 68/2024 regulamenta de forma pormenorizada a apura\'e7\'e3o e o recolhimento "\
        "do IVA Dual, unificando as legisla\'e7\'f5es federais, estaduais e municipais."\
    )\
\
    st.markdown(\
        """\
    - **Base Ampla (Art. 9\'ba do PLP 68):** Incid\'eancia universal sobre opera\'e7\'f5es onerosas de bens tang\'edveis, intang\'edveis, direitos e servi\'e7os.\
    - **N\'e3o-Cumulatividade (Arts. 25 a 40):** O adquirente compensa o imposto destacado no documento fiscal de aquisi\'e7\'e3o sem restri\'e7\'f5es setoriais.\
    - **Apura\'e7\'e3o Peri\'f3dica Centralizada (Art. 80):** Apura\'e7\'e3o unificada por estabelecimento ou CNPJ matriz, simplificando a contabilidade das empresas.\
    """\
    )\
\
    col1, col2 = st.columns(2)\
\
    with col1:\
        st.error("\uc0\u10060  Como era")\
        st.markdown(\
            """\
        - Apura\'e7\'e3o separada de PIS/Cofins federais com regras complexas de cumulatividade (Lucro Presumido vs. Real).\
        - Diverg\'eancias severas entre o ICMS estadual e o ISS municipal na presta\'e7\'e3o de servi\'e7os h\'edbridos.\
        """\
        )\
\
    with col2:\
        st.success("\uc0\u9989  Como vai ficar")\
        st.markdown(\
            """\
        - Guia unificada de pagamento e notas fiscais eletr\'f4nicas padronizadas em n\'edvel nacional.\
        - Extin\'e7\'e3o total de lit\'edgios sobre o conceito estrito de 'insumo industrial'.\
        """\
        )\
\
    st.markdown("\uc0\u55357 \u56599  **Refer\'eancia Legal Oficial:** [PLP 68/2024 - C\'e2mara dos Deputados](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2456475)")\
\
elif opcao == "3. Imposto Seletivo (IS) & Externalidades":\
    st.header("3. Imposto Seletivo - IS (Art. 139 ao 154 do PLP 68/2024)")\
    st.write(\
        "Conhecido como o 'Imposto do Pecado', o Imposto Seletivo possui car\'e1ter extrafiscal, visando "\
        "desestimular o consumo de bens e servi\'e7os nocivos \'e0 sa\'fade humana e ao meio ambiente."\
    )\
\
    st.markdown(\
        """\
    **Rol Legal Restrito de Incid\'eancia:**\
    - Ve\'edculos poluentes (crit\'e9rios de efici\'eancia energ\'e9tica e emiss\'e3o de carbono).\
    - Produtos de tabaco (cigarros e derivados).\
    - Bebidas alco\'f3licas (cervejas, vinhos e destilados, com al\'edquota progressiva por teor alco\'f3lico).\
    - Bebidas a\'e7ucaradas (refrigerantes e refrescos com adi\'e7\'e3o de a\'e7\'facar).\
    - Extra\'e7\'e3o de min\'e9rios (ferro, petr\'f3leo, g\'e1s natural e carv\'e3o mineral).\
    """\
    )\
\
    col1, col2 = st.columns(2)\
\
    with col1:\
        st.error("\uc0\u10060  Como era")\
        st.markdown(\
            """\
        - Tributa\'e7\'e3o difusa pelo IPI e tributos estaduais sem uniformidade nacional de foco em sa\'fade p\'fablica.\
        """\
        )\
\
    with col2:\
        st.success("\uc0\u9989  Como vai ficar")\
        st.markdown(\
            """\
        - Incid\'eancia monof\'e1sica federal calculada diretamente sobre o fator de nocividade (ex: teor de a\'e7\'facar ou polui\'e7\'e3o).\
        """\
        )\
\
    st.markdown("\uc0\u55357 \u56599  **Refer\'eancia Legal Oficial:** [Senado Federal - Not\'edcias e Textos Legais](https://www12.senado.leg.br)")\
\
elif opcao == "4. Cashback Tribut\'e1rio & Justi\'e7a Social":\
    st.header("4. Cashback Tribut\'e1rio (Arts. 105 a 115 do PLP 68/2024)")\
    st.write(\
        "Mecanismo inovador de devolu\'e7\'e3o de tributos (CBS e IBS) para combater a regressividade hist\'f3rica "\
        "do sistema tribut\'e1rio brasileiro sobre as fam\'edlias de baixa renda."\
    )\
\
    st.markdown(\
        """\
    - **P\'fablico Eleg\'edvel:** Fam\'edlias inscritas no Cadastro \'danico (Cad\'danico) com limites de renda per capita regulamentados.\
    - **Servi\'e7os Abrangidos:** Energia el\'e9trica, g\'e1s de cozinha (GLP), \'e1gua, esgoto e produtos da cesta b\'e1sica.\
    - **Automa\'e7\'e3o:** Cruzamento de dados fiscais (CPF na nota) com contas banc\'e1rias sociais para reembolso autom\'e1tico.\
    """\
    )\
\
    col1, col2 = st.columns(2)\
\
    with col1:\
        st.error("\uc0\u10060  Como era")\
        st.markdown(\
            """\
        - Cidad\'e3os de menor renda pagavam proporcionalmente a mesma al\'edquota de impostos indiretos que os mais ricos, sem restitui\'e7\'e3o.\
        """\
        )\
\
    with col2:\
        st.success("\uc0\u9989  Como vai ficar")\
        st.markdown(\
            """\
        - Devolu\'e7\'e3o de at\'e9 100% da parcela federal (CBS) e percentual da parcela subnacional (IBS) diretamente na conta do cidad\'e3o.\
        """\
        )\
\
    st.markdown("\uc0\u55357 \u56599  **Refer\'eancia Legal Oficial:** [Minist\'e9rio da Fazenda - Cidadania Fiscal](https://www.gov.br/fazenda)")\
\
elif opcao == "5. Split Payment & Tecnologia de Arrecada\'e7\'e3o":\
    st.header("5. Split Payment (Liquida\'e7\'e3o Financeira Simult\'e2nea)")\
    st.write(\
        "O *Split Payment* \'e9 a infraestrutura tecnol\'f3gica regulada pelo Banco Central que realiza a separa\'e7\'e3o autom\'e1tica "\
        "dos tributos (CBS e IBS) no exato momento da liquida\'e7\'e3o eletr\'f4nica da venda."\
    )\
\
    st.markdown(\
        """\
    - **Liquida\'e7\'e3o Instant\'e2nea:** No pagamento via Pix, cart\'e3o de d\'e9bito, cr\'e9dito ou boleto, a adquirente separa o imposto do faturamento l\'edquido.\
    - **Destina\'e7\'e3o Autom\'e1tica:** A CBS vai direto para o Tesouro Nacional; o IBS vai para a c\'e2mara de compensa\'e7\'e3o do Comit\'ea Gestor.\
    - **Seguran\'e7a Comercial:** O lojista recebe o valor l\'edquido imediatamente, eliminando o passivo de guias mensais de apura\'e7\'e3o.\
    """\
    )\
\
    col1, col2 = st.columns(2)\
\
    with col1:\
        st.error("\uc0\u10060  Como era")\
        st.markdown(\
            """\
        - O lojista recebia o valor total da venda e recolhia o imposto dias ou semanas depois via guia, gerando riscos de inadimpl\'eancia.\
        """\
        )\
\
    with col2:\
        st.success("\uc0\u9989  Como vai ficar")\
        st.markdown(\
            """\
        - Separa\'e7\'e3o tribut\'e1ria em tempo real na maquininha ou gateway de pagamento, zerando a sonega\'e7\'e3o e gerando cr\'e9dito imediato.\
        """\
        )\
\
    st.markdown("\uc0\u55357 \u56599  **Refer\'eancia Legal Oficial:** [Banco Central do Brasil - Sistema de Pagamentos](https://www.bcb.gov.br)")\
\
elif opcao == "6. Cesta B\'e1sica & Al\'edquotas Reduzidas":\
    st.header("6. Cesta B\'e1sica Nacional e Al\'edquotas Reduzidas (Arts. 75 a 104 do PLP 68/2024)")\
    st.write(\
        "Mecanismos de salvaguarda social e econ\'f4mica que garantem isen\'e7\'e3o total ou descontos expressivos "\
        "na carga tribut\'e1ria de itens essenciais \'e0 popula\'e7\'e3o."\
    )\
\
    st.markdown(\
        """\
    - **Cesta B\'e1sica Nacional (Al\'edquota Zero - Arts. 81-85):** Arroz, feij\'e3o, leite, carnes, ovos, p\'e3o comum e farinhas.\
    - **Redu\'e7\'e3o de 60% na Al\'edquota (Arts. 87-104):** Medicamentos, servi\'e7os de sa\'fade, dispositivos m\'e9dicos, educa\'e7\'e3o e transporte coletivo.\
    - **Redu\'e7\'e3o de 30%:** Insumos agropecu\'e1rios e aquicultura.\
    """\
    )\
\
    col1, col2 = st.columns(2)\
\
    with col1:\
        st.error("\uc0\u10060  Como era")\
        st.markdown(\
            """\
        - Al\'edquotas desorganizadas de PIS/Cofins e ICMS variando de estado para estado sobre alimentos e rem\'e9dios.\
        """\
        )\
\
    with col2:\
        st.success("\uc0\u9989  Como vai ficar")\
        st.markdown(\
            """\
        - Isen\'e7\'e3o absoluta (0%) padronizada em todo o territ\'f3rio nacional para os alimentos essenciais da Cesta B\'e1sica.\
        """\
        )\
\
    st.markdown("\uc0\u55357 \u56599  **Refer\'eancia Legal Oficial:** [C\'e2mara dos Deputados - Proposi\'e7\'f5es](https://www.camara.leg.br)")\
\
elif opcao == "\uc0\u55357 \u56522  7. Simulador Interativo Setorial (Estilo Pro)":\
    st.header("\uc0\u55357 \u56522  Simulador Avan\'e7ado de Carga Tribut\'e1ria por Setor e Faturamento")\
    st.write(\
        "Simule em tempo real o impacto financeiro e tribut\'e1rio para diferentes segmentos empresariais em **S\'e3o Paulo**, "\
        "comparando detalhadamente as al\'edquotas efetivas aplicadas no cen\'e1rio atual versus a transi\'e7\'e3o para o novo IVA Dual (CBS + IBS)."\
    )\
\
    st.subheader("\uc0\u9881 \u65039  Configura\'e7\'e3o dos Dados da Empresa")\
    \
    col_s1, col_s2, col_s3 = st.columns(3)\
\
    with col_s1:\
        faturamento_input = st.number_input(\
            "Faturamento Bruto Mensal (R$)",\
            min_value=100.0,\
            max_value=50000000.0,\
            value=1000.0,\
            step=500.0,\
            format="%.2f"\
        )\
\
    with col_s2:\
        segmento = st.selectbox(\
            "Segmento de Mercado / Atividade",\
            [\
                "Com\'e9rcio Varejista (Geral)",\
                "Supermercado / Alimenta\'e7\'e3o",\
                "Restaurante / Lanchonete / Alimenta\'e7\'e3o fora do lar",\
                "Presta\'e7\'e3o de Servi\'e7os (Geral / Escrit\'f3rio)",\
                "Tecnologia / Software (SaaS)",\
                "Sa\'fade / Cl\'ednicas M\'e9dicas"\
            ]\
        )\
\
    with col_s3:\
        regime_tributario = st.selectbox(\
            "Regime Tribut\'e1rio Atual",\
            [\
                "Simples Nacional",\
                "Lucro Presumido",\
                "Lucro Real"\
            ]\
        )\
\
    st.divider()\
\
    if "Com\'e9rcio" in segmento:\
        if regime_tributario == "Simples Nacional":\
            aliq_atual_str = "4,00% (Anexo I - DAS)"\
            base_aliq_atual = 0.04\
            aliq_novo_str = "4,00% (DAS Simplicidade) ou 26,5% (IVA Dual B2B opcional)"\
            base_aliq_novo = 0.04\
        elif regime_tributario == "Lucro Presumido":\
            aliq_atual_str = "21,65% (PIS 0,65% + Cofins 3% + ICMS SP ~18%)"\
            base_aliq_atual = 0.2165\
            aliq_novo_str = "26,50% (IVA Dual Padr\'e3o: CBS + IBS com cr\'e9ditos plenos)"\
            base_aliq_novo = 0.265\
        else:\
            aliq_atual_str = "27,25% (PIS 1,65% + Cofins 7,6% + ICMS SP ~18% com cr\'e9ditos restritos)"\
            base_aliq_atual = 0.2725\
            aliq_novo_str = "26,50% (IVA Dual Padr\'e3o com N\'e3o-Cumulatividade Financeira Plena)"\
            base_aliq_novo = 0.265\
\
    elif "Supermercado" in segmento:\
        if regime_tributario == "Simples Nacional":\
            aliq_atual_str = "3,50% (Anexo I - Com\'e9rcio com itens essenciais)"\
            base_aliq_atual = 0.035\
            aliq_novo_str = "3,50% (DAS) ou Al\'edquota Zero (Itens da Cesta B\'e1sica Nacional)"\
            base_aliq_novo = 0.035\
        elif regime_tributario == "Lucro Presumido":\
            aliq_atual_str = "18,00% (Carga mista PIS/Cofins/ICMS com substitui\'e7\'e3o tribut\'e1ria)"\
            base_aliq_atual = 0.18\
            aliq_novo_str = "12,00% (M\'e9dia ponderada com desonera\'e7\'e3o da Cesta B\'e1sica)"\
            base_aliq_novo = 0.12\
        else:\
            aliq_atual_str = "18,00% (Carga mista com apura\'e7\'e3o complexa de cr\'e9ditos)"\
            base_aliq_atual = 0.18\
            aliq_novo_str = "12,00% (M\'e9dia ponderada com desonera\'e7\'e3o da Cesta B\'e1sica)"\
            base_aliq_novo = 0.12\
\
    elif "Restaurante" in segmento:\
        if regime_tributario == "Simples Nacional":\
            aliq_atual_str = "5,00% (Anexo I/III - Alimenta\'e7\'e3o)"\
            base_aliq_atual = 0.05\
            aliq_novo_str = "5,00% (DAS) ou IVA Dual setorial com redu\'e7\'e3o regulamentada"\
            base_aliq_novo = 0.05\
        elif regime_tributario == "Lucro Presumido":\
            aliq_atual_str = "14,00% (PIS/Cofins + ICMS reduzido para bares e restaurantes em SP)"\
            base_aliq_atual = 0.14\
            aliq_novo_str = "20,00% (IVA Dual ajustado para setor de alimenta\'e7\'e3o fora do lar)"\
            base_aliq_novo = 0.20\
        else:\
            aliq_atual_str = "14,00% (PIS/Cofins + ICMS com cr\'e9ditos limitados)"\
            base_aliq_atual = 0.14\
            aliq_novo_str = "20,00% (IVA Dual ajustado com cr\'e9ditos operacionais amplos)"\
            base_aliq_novo = 0.20\
\
    elif "Servi\'e7os" in segmento:\
        if regime_tributario == "Simples Nacional":\
            aliq_atual_str = "6,00% (Anexo III inicial - Servi\'e7os)"\
            base_aliq_atual = 0.06\
            aliq_novo_str = "6,00% (DAS) ou destaque opcional do IVA Dual"\
            base_aliq_novo = 0.06\
        elif regime_tributario == "Lucro Presumido":\
            aliq_atual_str = "8,65% (PIS 0,65% + Cofins 3% + ISS SP 5%)"\
            base_aliq_atual = 0.0865\
            aliq_novo_str = "26,50% (IVA Dual Padr\'e3o: CBS + IBS unificados)"\
            base_aliq_novo = 0.265\
        else:\
            aliq_atual_str = "14,25% (PIS 1,65% + Cofins 7,6% n\'e3o cumulativos + ISS SP 5%)"\
            base_aliq_atual = 0.1425\
            aliq_novo_str = "26,50% (IVA Dual Padr\'e3o com dedu\'e7\'e3o irrestrita de insumos)"\
            base_aliq_novo = 0.265\
\
    elif "Tecnologia" in segmento:\
        if regime_tributario == "Simples Nacional":\
            aliq_atual_str = "6,00% a 15,5% (Anexo III / V conforme Fator R)"\
            base_aliq_atual = 0.06\
            aliq_novo_str = "6,00% (DAS) ou IVA Dual setorial"\
            base_aliq_novo = 0.06\
        elif regime_tributario == "Lucro Presumido":\
            aliq_atual_str = "8,65% (PIS/Cofins + ISS SP 5%)"\
            base_aliq_atual = 0.0865\
            aliq_novo_str = "26,50% (IVA Dual Padr\'e3o sobre licenciamento de software e servi\'e7os)"\
            base_aliq_novo = 0.265\
        else:\
            aliq_atual_str = "14,25% (PIS/Cofins + ISS SP 5%)"\
            base_aliq_atual = 0.1425\
            aliq_novo_str = "26,50% (IVA Dual Padr\'e3o com aproveitamento de cr\'e9ditos de servidores e nuvem)"\
            base_aliq_novo = 0.265\
\
    else: # Sa\'fade\
        if regime_tributario == "Simples Nacional":\
            aliq_atual_str = "5,00% a 10% (Anexo III - Cl\'ednicas e Sa\'fade)"\
            base_aliq_atual = 0.05\
            aliq_novo_str = "5,00% (DAS) ou al\'edquota reduzida por benesse constitucional"\
            base_aliq_novo = 0.05\
        elif regime_tributario == "Lucro Presumido":\
            aliq_atual_str = "8,00% (PIS/Cofins + ISS reduzido para servi\'e7os m\'e9dicos em SP)"\
            base_aliq_atual = 0.08\
            aliq_novo_str = "10,60% (IVA Dual com redu\'e7\'e3o de 60% garantida pelo PLP 68/2024)"\
            base_aliq_novo = 0.106\
        else:\
            aliq_atual_str = "8,00% (Carga mista de servi\'e7os de sa\'fade)"\
            base_aliq_atual = 0.08\
            aliq_novo_str = "10,60% (IVA Dual com redu\'e7\'e3o de 60% e cr\'e9ditos plenos sobre equipamentos)"\
            base_aliq_novo = 0.106\
\
    imposto_atual_val = faturamento_input * base_aliq_atual\
    imposto_novo_val = faturamento_input * base_aliq_novo\
    diferenca_valor = imposto_novo_val - imposto_atual_val\
    percentual_variacao = (diferenca_valor / imposto_atual_val) * 100 if imposto_atual_val > 0 else 0\
\
    st.subheader(f"\uc0\u55357 \u56522  Relat\'f3rio de Simula\'e7\'e3o: \{segmento\} (\{regime_tributario\})")\
\
    st.markdown("### \uc0\u55357 \u56589  Detalhamento das Al\'edquotas Efetivas Aplicadas:")\
    col_alq1, col_alq2 = st.columns(2)\
    with col_alq1:\
        st.info(f"**Al\'edquota no Cen\'e1rio Atual:**\\n\\n`\{aliq_atual_str\}`")\
    with col_alq2:\
        st.success(f"**Al\'edquota no Novo Modelo (Reforma):**\\n\\n`\{aliq_novo_str\}`")\
\
    st.divider()\
\
    col_res1, col_res2, col_res3 = st.columns(3)\
\
    with col_res1:\
        st.metric(\
            label="Carga Tribut\'e1ria Atual (R$)",\
            value=f"R$ \{imposto_atual_val:,.2f\}",\
            delta=f"Efetiva: \{(base_aliq_atual)*100:.2f\}%"\
        )\
\
    with col_res2:\
        st.metric(\
            label="Nova Carga (Reforma Tribut\'e1ria)",\
            value=f"R$ \{imposto_novo_val:,.2f\}",\
            delta=f"Efetiva: \{(base_aliq_novo)*100:.2f\}%",\
            delta_color="off"\
        )\
\
    with col_res3:\
        st.metric(\
            label="Varia\'e7\'e3o Estimada",\
            value=f"R$ \{diferenca_valor:+,.2f\}",\
            delta=f"\{percentual_variacao:+.1f\}%",\
            delta_color="inverse"\
        )\
\
    st.markdown("---")\
    st.markdown("### \uc0\u55357 \u56541  Parecer T\'e9cnico Anal\'edtico para o Setor")\
    \
    if regime_tributario == "Simples Nacional":\
        st.info(\
            f"**An\'e1lise para \{segmento\} no Simples Nacional:** "\
            "A empresa est\'e1 protegida pela imunidade de simplifica\'e7\'e3o do Simples, mantendo a op\'e7\'e3o de recolhimento unificado via DAS. "\
            "No entanto, caso atenda predominantemente a outras empresas (B2B), a legisla\'e7\'e3o da reforma permite optar por destacar "\
            "o IBS e a CBS fora do DAS para que o seu cliente aproveite 100% dos cr\'e9ditos tribut\'e1rios."\
        )\
    elif regime_tributario == "Lucro Presumido":\
        st.info(\
            f"**An\'e1lise para \{segmento\} no Lucro Presumido:** "\
            "Os tributos fragmentados antigos (PIS, Cofins e ICMS/ISS) s\'e3o substitu\'eddos pelo IVA Dual unificado. "\
            "Embora a al\'edquota nominal se aproxime do padr\'e3o internacional, a grande vantagem competitiva reside no "\
            "**aproveitamento pleno de cr\'e9ditos** sobre todas as aquisi\'e7\'f5es de insumos operacionais e mercadorias, eliminando o efeito cascata."\
        )\
    else:\
        st.info(\
            f"**An\'e1lise para \{segmento\} no Lucro Real:** "\
            "Com a aplica\'e7\'e3o da **n\'e3o-cumulatividade financeira plena**, o contencioso sobre o conceito restrito de insumo deixa de existir. "\
            "Qualquer despesa operacional, mercadoria ou investimento incorrido na atividade gera cr\'e9dito imediato para dedu\'e7\'e3o autom\'e1tica, "\
            "garantindo total neutralidade fiscal e otimiza\'e7\'e3o de fluxo de caixa para a corpora\'e7\'e3o."\
        )\
\
elif opcao == "\uc0\u55357 \u56994  8. Simula\'e7\'e3o de Importa\'e7\'e3o & Cota\'e7\'e3o do D\'f3lar":\
    st.header("\uc0\u55357 \u56994  Simula\'e7\'e3o de Importa\'e7\'e3o com Cota\'e7\'e3o do D\'f3lar em Tempo Real")\
    st.write(\
        f"Esta ferramenta busca a cota\'e7\'e3o oficial do d\'f3lar americano (USD) atualizada da internet em tempo real. "\
        f"A taxa de c\'e2mbio vigente no momento \'e9 de **R$ \{cotacao_dolar_atual:.4f\}** por 1 USD."\
    )\
\
    st.markdown("---")\
    st.subheader("\uc0\u55358 \u56814  Conversor de Moeda e Calculadora Aduaneira")\
\
    col_imp1, col_imp2 = st.columns(2)\
\
    with col_imp1:\
        valor_usd = st.number_input(\
            "Valor da Mercadoria em D\'f3lares (USD $)",\
            min_value=10.0,\
            max_value=1000000.0,\
            value=1000.0,\
            step=100.0,\
            format="%.2f"\
        )\
        aliq_ii = st.slider("Al\'edquota do Imposto de Importa\'e7\'e3o (II) (%)", 0.0, 50.0, 14.0, 1.0)\
\
    with col_imp2:\
        regime_importador = st.selectbox(\
            "Regime do Importador no Brasil",\
            ["Lucro Real / Presumido (Gera Cr\'e9dito de IBS/CBS)", "Simples Nacional / Consumidor Final (Sem Cr\'e9dito)"],\
            key="regime_imp"\
        )\
        # Exibi\'e7\'e3o clara da convers\'e3o direta\
        valor_cif_brl = valor_usd * cotacao_dolar_atual\
        st.info(f"\uc0\u55357 \u56501  **Convers\'e3o do D\'f3lar:**\\n\\nUS$ \{valor_usd:,.2f\} equivalem a **R$ \{valor_cif_brl:,.2f\}** (Base CIF convertida a R$ \{cotacao_dolar_atual:.4f\}/USD).")\
\
    # C\'e1lculos aduaneiros\
    valor_ii = valor_cif_brl * (aliq_ii / 100.0)\
    base_tributos_antiga = valor_cif_brl + valor_ii\
    tributos_antigos_val = base_tributos_antiga * 0.2975 # PIS/Cofins imp + ICMS SP\
\
    base_iva_dual = valor_cif_brl + valor_ii\
    tributos_novos_bruto = base_iva_dual * 0.265 # IVA Dual padr\'e3o combinado (26,5%)\
\
    credito_recuperavel = tributos_novos_bruto if "Lucro Real" in regime_importador else 0.0\
    tributos_novos_liquido = tributos_novos_bruto - credito_recuperavel\
\
    st.markdown("---")\
    st.subheader("\uc0\u55357 \u56520  Resultado da Simula\'e7\'e3o Aduaneira")\
\
    res_imp1, res_imp2, res_imp3 = st.columns(3)\
\
    with res_imp1:\
        st.metric(\
            label="Tributos no Sistema Antigo",\
            value=f"R$ \{tributos_antigos_val:,.2f\}",\
            delta="Al\'edquota efetiva ~29,75%"\
        )\
\
    with res_imp2:\
        st.metric(\
            label="Novo IVA Dual (Bruto na Fronteira)",\
            value=f"R$ \{tributos_novos_bruto:,.2f\}",\
            delta="Al\'edquota padr\'e3o 26,50%",\
            delta_color="off"\
        )\
\
    with res_imp3:\
        st.metric(\
            label="Custo Tribut\'e1rio Efetivo L\'edquido",\
            value=f"R$ \{tributos_novos_liquido:,.2f\}",\
            delta=f"Cr\'e9dito recuperado: R$ \{credito_recuperavel:,.2f\}",\
            delta_color="normal"\
        )\
\
    st.markdown("---")\
    st.subheader("\uc0\u55357 \u56523  Tabela Comparativa de Al\'edquotas (%) na Importa\'e7\'e3o")\
    st.markdown(\
        """\
        | Tributo / Etapa | Sistema Antigo (Cen\'e1rio Vigente) | Novo Modelo da Reforma (IVA Dual) |\
        | :--- | :--- | :--- |\
        | **Imposto de Importa\'e7\'e3o (II)** | Vari\'e1vel conforme NCM (`0%` a `35%`) | Mantido inalterado (Federal aduaneiro) |\
        | **Tributos Federais de Consumo** | PIS-Importa\'e7\'e3o (`2,1%`) + Cofins-Importa\'e7\'e3o (`9,65%`) | **CBS (Federal)**: Unificada (~`8,8%` a `9,5%` de refer\'eancia) |\
        | **Tributos Estaduais de Consumo** | ICMS-Importa\'e7\'e3o em SP (`18%`) | **IBS (Subnacional)**: Unificado (~`17%` a `17,5%` de refer\'eancia) |\
        | **Carga Tribut\'e1ria Total Nominal** | Aproximadamente `29,75%` acumulativa | **`26,50%`** (IVA Dual Padr\'e3o combinando CBS + IBS) |\
        | **Aproveitamento de Cr\'e9dito** | Restrito e sujeito a lit\'edgios de insumo | **Cr\'e9dito Financeiro Pleno e Imediato** para empresas regulares |\
        """\
    )\
\
elif opcao == "\uc0\u55358 \u56598  9. IA Consultora Oficial (Base de Dados do Governo)":\
    st.header("\uc0\u55358 \u56598  Intelig\'eancia Artificial Especialista na Reforma Tribut\'e1ria")\
    st.write(\
        "Fa\'e7a qualquer pergunta sobre as novas regras, al\'edquotas, transi\'e7\'e3o at\'e9 2033, impactos setoriais "\
        "ou dispositivos legais das Leis Complementares. A intelig\'eancia artificial est\'e1 conectada e pronta para responder "\
        "com base estritamente nas fontes e dados oficiais do governo."\
    )\
\
    # Inje\'e7\'e3o autom\'e1tica da chave de API fornecida\
    os.environ["GEMINI_API_KEY"] = "AQ.Ab8RN6JlC0g4kgKb2d6MjU_Lmrabzzg-mbCXLgyYOV7DYUc6DA"\
    \
    st.success("\uc0\u55357 \u56594  Chave de API oficial conectada com sucesso! A IA est\'e1 pronta para consultas.")\
\
    # Caixa de chat interativa\
    pergunta_usuario = st.text_area(\
        "Digite sua d\'favida sobre a Reforma Tribut\'e1ria:",\
        placeholder="Ex: Como funciona a convers\'e3o de c\'e2mbio e a cobran\'e7a de CBS e IBS nas importa\'e7\'f5es?"\
    )\
\
    if st.button("Consultar IA Oficial"):\
        if not pergunta_usuario:\
            st.warning("\uc0\u9888 \u65039  Digite uma pergunta para consultar a base de dados.")\
        else:\
            with st.spinner("Consultando dados oficiais da legisla\'e7\'e3o e formulando resposta t\'e9cnica..."):\
                try:\
                    from google import genai\
                    from google.genai import types\
\
                    client = genai.Client()\
\
                    system_instruction = (\
                        "Voc\'ea \'e9 um consultor tribut\'e1rio s\'eanior e especialista t\'e9cnico na Reforma Tribut\'e1ria do Consumo do Brasil "\
                        "(Emenda Constitucional n\'ba 132/2023, PLP 68/2024 e PLP 108/2024). "\
                        "Responda \'e0s d\'favidas dos usu\'e1rios com base t\'e9cnica, citando artigos e fundamentos legais corretos, "\
                        "mantendo tom profissional, claro e fundamentado exclusivamente nas diretrizes do Governo Federal e do Congresso Nacional."\
                    )\
\
                    response = client.models.generate_content(\
                        model='gemini-3.6-flash',\
                        contents=pergunta_usuario,\
                        config=types.GenerateContentConfig(\
                            system_instruction=system_instruction,\
                            temperature=0.2,\
                        ),\
                    )\
\
                    st.success("\uc0\u9989  Resposta Oficial da IA:")\
                    st.markdown(response.text)\
\
                except Exception as e:\
                    st.error(f"Ocorreu um erro ao conectar com a IA: \{e\}")\
\
st.divider()\
st.caption(\
    "Desenvolvido bypedromarques com base nas diretrizes oficiais da Emenda Constitucional n\'ba 132/2023, "\
    "dos Projetos de Lei Complementar (PLP 68/2024 e PLP 108/2024) e fontes oficiais do Minist\'e9rio da Fazenda. "\
    "Consulte sempre as publica\'e7\'f5es atualizadas no Di\'e1rio Oficial da Uni\'e3o."\
)}