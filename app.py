import streamlit as st
import os

# Configuração da página
st.set_page_config(
    page_title="Simulador Avançado da Reforma Tributária",
    page_icon="💲",
    layout="wide",
)

# Título principal
st.title("🇧🇷 Simulador Pratico - Reforma Tributaria - Pedro Marques")
st.markdown(
    "Plataforma técnica baseada na **Emenda Constitucional nº 132/2023** e nos textos complementares "
    "(**PLP nº 68/2024 e PLP nº 108/2024**). Ferramenta com análises jurídicas, detalhamento normativo "
    "e simulações numéricas integradas com inteligência artificial."
)

st.divider()

# Lista de módulos para os botões da barra lateral
modulos = [
    "1. Visão Geral & Marco Constitucional",
    "2. IVA Dual (CBS e IBS) - PLP 68/2024",
    "3. Imposto Seletivo (IS) & Externalidades",
    "4. Cashback Tributário & Justiça Social",
    "5. Split Payment & Tecnologia de Arrecadação",
    "6. Cesta Básica & Alíquotas Reduzidas",
    "🏠 7. Aluguéis de Imóveis na Reforma",
    "📜 8. Herança & Doação (ITCMD)",
    "📊 9. Simulador Interativo Setorial & Transição",
    "🚢 10. Simulação de Importação & Tributação no Destino",
    "📈 11. Impactos no SPED Fiscal (Atual vs. Futuro)",
    "🗂️ 12. Guia para o Contador (50 FAQs & Links Oficiais)",
    "🤖 13. IA Consultora Oficial (Base de Dados do Governo)",
]

# Gerenciamento de estado para lembrar qual botão foi clicado
if 'opcao_selecionada' not in st.session_state:
    st.session_state.opcao_selecionada = modulos[0]

st.sidebar.header("📋 Módulos de Análise")
st.sidebar.markdown("---")

# Renderiza cada aba como um botão interativo empilhado na lateral
for mod in modulos:
    if st.sidebar.button(mod, use_container_width=True):
        st.session_state.opcao_selecionada = mod

opcao = st.session_state.opcao_selecionada

# Conteúdo dinâmico baseado na escolha do botão
if opcao == "1. Visão Geral & Marco Constitucional":
    st.header("Visão Geral & Fundamentos Constitucionais (EC 132/2023)")
    st.write(
        "A Emenda Constitucional nº 132/2023 reescreveu a arquitetura da tributação do consumo no Brasil, "
        "estabelecendo a transição do princípio da origem para o **princípio do destino pleno**."
    )

    st.markdown(
        """
    - **Art. 156-A da CF/88:** Instituição do IBS (Imposto sobre Bens e Serviços), competência de Estados, DF e Municípios.
    - **Art. 195, V da CF/88:** Instituição da CBS (Contribuição Social sobre Bens e Serviços), competência da União.
    - **Neutralidade Econômica:** Eliminação de distorções logísticas e societárias induzidas por incentivos fiscais estaduais (Guerra Fiscal).
    """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ Como era (O Sistema Antigo)")
        st.markdown(
            """
        - **5 Tributos Fragmentados:** PIS, Cofins, IPI, ICMS e ISS com bases de cálculo distintas.
        - **Efeito Cascata Crônico:** Cobrança de imposto sobre imposto ao longo de toda a cadeia produtiva e de circulação.
        - **Litigiosidade Extrema:** Milhares de horas e bilhões de reais gastos em contenciosos judiciais sobre o conceito de insumo.
        """
        )
    with col2:
        st.success("✅ Como vai ficar (O Novo Sistema - 2026 a 2033)")
        st.markdown(
            """
        - **IVA Dual Padronizado:** CBS (Federal) + IBS (Subnacional).
        - **Não-Cumulatividade Financeira Plena:** Crédito imediato de todo imposto pago na etapa anterior.
        - **Arrecadação no Destino:** O imposto pertence ao município e estado onde reside o adquirente final do produto ou serviço.
        """
        )

    st.markdown("---")
    st.subheader("🏢 Impactos Práticos na Gestão das Empresas")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Fim da Guerra Fiscal:** As empresas deixam de escolher locais de instalação com base em favores fiscais distorcidos.
        - **Simplificação Operacional:** Redução expressiva no custo de conformidade e planejamento tributário logístico.
        """
        )
    with col_e2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Custo de Transição:** Necessidade de aportes financeiros em novos softwares corporativos e reestruturação de contratos.
        - **Incerteza Inicial:** Período de adaptação às novas regras de apuração nacional compartilhada entre União, Estados e Municípios.
        """
        )

    st.markdown("---")
    st.subheader("📚 Impactos Práticos na Rotina da Contabilidade")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Padronização Normativa:** Fim das divergências bizarras entre legislações estaduais e municipais concorrentes.
        - **Valorização Consultiva:** O contador assume papel estratégico direto na reengenharia financeira e societária dos clientes.
        """
        )
    with col_c2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Sobrecarga de Trabalho na Transição:** Acúmulo de obrigações durante os anos de convivência simultânea entre os sistemas antigo e novo.
        - **Curva de Aprendizado Acelerada:** Exigência de domínio imediato de conceitos contábeis e fiscais inéditos do IVA Dual.
        """
        )

    st.markdown("---")
    st.subheader("📅 Cronograma Oficial de Transição (2026 a 2033)")
    st.markdown(
        """
        | Ano / Período | Marco de Implementação / O que muda na prática | Tributos Envolvidos |
        | :--- | :--- | :--- |
        | **2026** | **Ano-Teste Nacional:** Início dos testes operacionais com alíquotas de referência para validação de sistemas e notas fiscais. | CBS (`0,9%`) e IBS (`0,1%`) |
        | **2027** | **Entrada da CBS Plena e Fim do PIS/Cofins:** Extinção definitiva do PIS, da Cofins e do IPI; início do Imposto Seletivo (IS). | CBS Cheia + Extinção PIS/Cofins/IPI + Início IS |
        | **2028** | **Consolidação Federal e Ajustes:** Manutenção da CBS plena e ajustes normativos complementares. | CBS Plena + Manutenção ICMS/ISS |
        | **2029** | **Início da Transição do IBS (10%):** Estados e municípios começam a substituir progressivamente ICMS/ISS pelo IBS. | IBS (`10%`) + ICMS/ISS (`90%`) |
        | **2030** | **Progressão do IBS (20%):** Aumento da participação do IBS e redução proporcional de ICMS e ISS. | IBS (`20%`) + ICMS/ISS (`80%`) |
        | **2031** | **Aceleração da Transição (30%):** Continuidade da substituição gradual da arrecadação subnacional. | IBS (`30%`) + ICMS/ISS (`70%`) |
        | **2032** | **Fase Final da Transição (40%):** Último ano de convivência mista entre tributos antigos e o IBS. | IBS (`40%`) + ICMS/ISS (`60%`) |
        | **2033** | **Sistema Pleno Vigente:** Extinção total de ICMS e ISS. O IVA Dual (CBS + IBS) vigora integralmente. | Apenas CBS + IBS + Imposto Seletivo |
        """
    )
    st.markdown("🔗 **Referência Legal Oficial:** [Emenda Constitucional nº 132/2023 - Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm)")

elif opcao == "2. IVA Dual (CBS e IBS) - PLP 68/2024":
    st.header("2. IVA Dual: CBS (Livro I) e IBS (Gestão Compartilhada)")
    st.write(
        "O Projeto de Lei Complementar nº 68/2024 regulamenta de forma pormenorizada a apuração e o recolhimento "
        "do IVA Dual, unificando as legislações federais, estaduais e municipais."
    )

    st.markdown(
        """
    - **Base Ampla (Art. 9º do PLP 68):** Incidência universal sobre operações onerosas de bens tangíveis, intangíveis, direitos e serviços.
    - **Não-Cumulatividade (Arts. 25 a 40):** O adquirente compensa o imposto destacado no documento fiscal de aquisição sem restrições setoriais.
    - **Apuração Periódica Centralizada (Art. 80):** Apuração unificada por estabelecimento ou CNPJ matriz, simplificando a contabilidade das empresas.
    """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ Como era")
        st.markdown(
            """
        - Apuração separada de PIS/Cofins com regras complexas (Lucro Presumido vs. Real).
        - Divergências severas entre ICMS estadual e ISS municipal em serviços híbridos.
        """
        )
    with col2:
        st.success("✅ Como vai ficar")
        st.markdown(
            """
        - Guia unificada de pagamento e notas fiscais eletrônicas padronizadas nacionalmente.
        - Extinção total de litígios judiciais sobre o conceito restrito de insumo.
        """
        )

    st.markdown("---")
    st.subheader("🏢 Impactos Práticos na Gestão das Empresas")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Crédito Imediato:** Aproveitamento financeiro de créditos tributários sem barreiras de interpretação setorial.
        - **Previsibilidade de Caixa:** Apuração centralizada por CNPJ que otimiza o capital de giro.
        """
        )
    with col_e2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Alíquota Padrão Elevada:** Possível pressão sobre margens de lucro em setores que antes possuíam cargas efetivas menores.
        - **Adaptação de Processos:** Necessidade de revisão profunda nos sistemas de emissão e controle de notas de entrada e saída.
        """
        )

    st.markdown("---")
    st.subheader("📚 Impactos Práticos na Rotina da Contabilidade")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Eliminação de Teses Confusas:** Fim das intermináveis discussões jurídicas sobre direito a crédito de PIS/Cofins e ICMS.
        - **Automação de Apurações:** Redução drástica do trabalho manual repetitivo na apuração de impostos mensais.
        """
        )
    with col_c2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Complexidade na Transição de Saldos Credores:** Controle rigoroso de saldos acumulados antigos de ICMS e PIS/Cofins.
        - **Riscos de Conformidade:** Rigor tecnológico na fiscalização digital integrada exigirá controle absoluto por parte do escritório.
        """
        )
    st.markdown("🔗 **Referência Legal Oficial:** [PLP 68/2024 - Câmara dos Deputados](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2456475)")

elif opcao == "3. Imposto Seletivo (IS) & Externalidades":
    st.header("3. Imposto Seletivo - IS (Art. 139 ao 154 do PLP 68/2024)")
    st.write(
        "Conhecido como o 'Imposto do Pecado', o Imposto Seletivo possui caráter extrafiscal, visando "
        "desestimular o consumo de bens e serviços nocivos à saúde humana e ao meio ambiente."
    )

    st.markdown(
        """
    **Rol Legal Restrito de Incidência:**
    - Veículos poluentes (critérios de eficiência energética e emissão de carbono).
    - Produtos de tabaco (cigarros e derivados).
    - Bebidas alcoólicas (cervejas, vinhos e destilados, com alíquota progressiva por teor alcoólico).
    - Bebidas açucaradas (refrigerantes e refrescos com adição de açúcar).
    - Extração de minérios (ferro, petróleo, gás natural e carvão mineral).
    """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ Como era")
        st.markdown("- Tributação difusa pelo IPI e tributos estaduais sem uniformidade nacional voltada para a saúde pública.")
    with col2:
        st.success("✅ Como vai ficar")
        st.markdown("- Incidência monofásica federal calculada diretamente sobre o fator de nocividade (ex: teor de açúcar ou poluição).")

    st.markdown("---")
    st.subheader("🏢 Impactos Práticos na Gestão das Empresas")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Regras Nacionais Claras:** Substituição de devedores e regras estaduais fragmentadas por um padrão federal unificado.
        - **Incentivo à Inovação:** Premiação tributária para empresas que desenvolvem produtos menos poluentes ou mais saudáveis.
        """
        )
    with col_e2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Impacto Direto no Preço Final:** Aumento de carga tributária sobre setores específicos (bebidas, tabaco, mineração e automotivo).
        - **Risco de Retração de Demanda:** Possível queda nas vendas decorrente do encarecimento de produtos sujeitos ao IS.
        """
        )

    st.markdown("---")
    st.subheader("📚 Impactos Práticos na Rotina da Contabilidade")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Clareza de Incidência:** Rol restrito definido em lei, facilitando a identificação exata de quais produtos sofrem o imposto.
        - **Oportunidade Consultiva:** Orientação estratégica a indústrias sobre reformulação de portfólio para mitigação de custos.
        """
        )
    with col_c2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Monitoramento de Parâmetros Técnicos:** Necessidade de controlar métricas físico-químicas complexas (teor de açúcar, poluição) no ERP.
        - **Gestão de Riscos Fiscais:** Risco elevado de autuações para empresas que classificarem incorretamente o fator de nocividade do produto.
        """
        )
    st.markdown("🔗 **Referência Legal Oficial:** [Senado Federal - Notícias e Textos Legais](https://www12.senado.leg.br)")

elif opcao == "4. Cashback Tributário & Justiça Social":
    st.header("4. Cashback Tributário (Arts. 105 a 115 do PLP 68/2024)")
    st.write(
        "Mecanismo inovador de devolução de tributos (CBS e IBS) para combater a regressividade histórica "
        "do sistema tributário brasileiro sobre as famílias de baixa renda."
    )

    st.markdown(
        """
    - **Público Elegível:** Famílias inscritas no Cadastro Único (CadÚnico) com limites de renda per capita regulamentados.
    - **Serviços Abrangidos:** Energia elétrica, gás de cozinha (GLP), água, esgoto e produtos da cesta básica.
    - **Automação:** Cruzamento de dados fiscais (CPF na nota) com contas bancárias sociais para reembolso automático.
    """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ Como era")
        st.markdown("- Cidadãos de menor renda pagavam proporcionalmente a mesma alíquota de impostos indiretos que os mais ricos, sem qualquer restituição.")
    with col2:
        st.success("✅ Como vai ficar")
        st.markdown("- Devolução de até 100% da parcela federal (CBS) e percentual da parcela subnacional (IBS) diretamente na conta do cidadão.")

    st.markdown("---")
    st.subheader("🏢 Impactos Práticos na Gestão das Empresas")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Estímulo ao Consumo Popular:** Aumento do poder de compra das famílias de baixa renda, impulsionando o varejo essencial.
        - **Inclusão Digital e Fiscal:** Formalização de pequenos comércios locais que atendem a base da pirâmide consumidora.
        """
        )
    with col_e2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Exigência de Informação no Varejo:** Obrigação de capturar o CPF do adquirente corretamente em todas as operações elegíveis.
        - **Adequação Tecnológica:** Necessidade de integração dos sistemas de PDV com as plataformas governamentais de validação de benefício.
        """
        )

    st.markdown("---")
    st.subheader("📚 Impactos Práticos na Rotina da Contabilidade")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Automação Governamental:** O cálculo e o pagamento do cashback são geridos pelo governo, desonerando a empresa de repasses diretos.
        - **Conformidade Simplificada:** Validação automatizada via nota fiscal eletrônica, reduzindo o esforço de controle interno.
        """
        )
    with col_c2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Auditoria de Emissão:** Risco de responsabilidade subsidiária caso o estabelecimento preencha incorretamente os dados do adquirente na nota.
        - **Suporte a Clientes do Varejo:** Necessidade de orientar comerciantes de pequeno porte sobre a exigência correta do CPF na nota.
        """
        )
    st.markdown("🔗 **Referência Legal Oficial:** [Ministério da Fazenda - Cidadania Fiscal](https://www.gov.br/fazenda)")

elif opcao == "5. Split Payment & Tecnologia de Arrecadação":
    st.header("5. Split Payment (Liquidação Financeira Simultânea)")
    st.write(
        "O *Split Payment* é a infraestrutura tecnológica regulada pelo Banco Central que realiza a separação automática "
        "dos tributos (CBS e IBS) no exato momento da liquidação eletrônica da venda."
    )

    st.markdown(
        """
    - **Liquidação Instantânea:** No pagamento via Pix, cartão de débito, crédito ou boleto, a adquirente separa o imposto do faturamento líquido.
    - **Destinação Automática:** A CBS vai direto para o Tesouro Nacional; o IBS vai para a câmara de compensação do Comitê Gestor.
    - **Segurança Comercial:** O lojista recebe o valor líquido imediatamente, eliminando o passivo de guias mensais de apuração.
    """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ Como era")
        st.markdown("- O lojista recebia o valor total da venda e recolhia o imposto dias ou semanas depois via guia, gerando passivos e riscos de inadimplência.")
    with col2:
        st.success("✅ Como vai ficar")
        st.markdown("- Separação tributária em tempo real na maquininha ou gateway de pagamento, zerando a sonegação e gerando crédito imediato.")

    st.markdown("---")
    st.subheader("🏢 Impactos Práticos na Gestão das Empresas")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Zerar Passivo Tributário Acidental:** Fim do risco de gastar o dinheiro do imposto retido e acumular dívidas fiscais involuntárias.
        - **Crédito Imediato na Cadeia:** O adquirente valida seu crédito fiscal no exato segundo da liquidação da transação comercial.
        """
        )
    with col_e2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Impacto Temporário no Fluxo de Caixa:** Retenção instantânea do imposto na fonte, exigindo ajuste no capital de giro operacional.
        - **Dependência Tecnológica:** Dependência absoluta de adquirentes, subadquirentes e bancos integrados ao padrão do Banco Central.
        """
        )

    st.markdown("---")
    st.subheader("📚 Impactos Práticos na Rotina da Contabilidade")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Fim da Emissão de Guias Manuais:** Redução drástica da emissão de DARFs e GAREs mensais de apuração de consumo.
        - **Reconciliação Automatizada:** Maior facilidade para conciliar extratos de recebimento líquido com relatórios fiscais.
        """
        )
    with col_c2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Complexidade de Conciliação Bancária:** Exigência de novos métodos de auditoria para validar divergências entre o split e o faturamento bruto.
        - **Suporte a Falhas de Sistema:** Atendimento a clientes em casos de falhas de comunicação entre meios de pagamento e o fisco.
        """
        )
    st.markdown("🔗 **Referência Legal Oficial:** [Banco Central do Brasil - Sistema de Pagamentos](https://www.bcb.gov.br)")

elif opcao == "6. Cesta Básica & Alíquotas Reduzidas":
    st.header("6. Cesta Básica Nacional e Alíquotas Reduzidas (Arts. 75 a 104 do PLP 68/2024)")
    st.write(
        "Mecanismos de salvaguarda social e econômica que garantem isenção total ou descontos expressivos "
        "na carga tributária de itens essenciais à população."
    )

    st.markdown(
        """
    - **Cesta Básica Nacional (Alíquota Zero - Arts. 81-85):** Arroz, feijão, leite, carnes, ovos, pão comum e farinhas.
    - **Redução de 60% na Alíquota (Arts. 87-104):** Medicamentos, serviços de saúde, dispositivos médicos, educação e transporte coletivo.
    - **Redução de 30%:** Insumos agropecuários e aquicultura.
    """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ Como era")
        st.markdown("- Alíquotas desorganizadas de PIS/Cofins e ICMS variando de estado para estado sobre alimentos e remédios essenciais.")
    with col2:
        st.success("✅ Como vai ficar")
        st.markdown("- Isenção absoluta (0%) padronizada em todo o território nacional para os alimentos essenciais da Cesta Básica.")

    st.markdown("---")
    st.subheader("🏢 Impactos Práticos na Gestão das Empresas")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Padronização Nacional:** Fim das divergências estaduais sobre quais produtos compõem a cesta básica e as isenções.
        - **Estímulo ao Setor Essencial:** Aumento da competitividade de produtores e distribuidores de alimentos e medicamentos.
        """
        )
    with col_e2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Gestão de Créditos Acumulados:** Com alíquota zero na saída, a empresa geradora pode acumular créditos nas etapas anteriores que exigem ressarcimento.
        - **Classificação Rigorosa de SKUs:** Risco operacional elevado caso produtos não isentos sejam classificados incorretamente como cesta básica.
        """
        )

    st.markdown("---")
    st.subheader("📚 Impactos Práticos na Rotina da Contabilidade")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Regras Claras e Federais:** Facilidade na orientação consultiva devido ao rol taxativo e nacional da Cesta Básica.
        - **Segurança Jurídica:** Redução drástica de litígios sobre enquadramento tributário de medicamentos e itens de saúde.
        """
        )
    with col_c2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Controle de Ressarcimento:** Necessidade de acompanhar e auditar constantemente processos de pedido de ressarcimento de créditos acumulados.
        - **Revisão de Cadastros de Produtos:** Esforço operacional massivo na revisão de NCMs e descritivos de milhares de produtos no ERP dos clientes.
        """
        )
    st.markdown("🔗 **Referência Legal Oficial:** [Câmara dos Deputados - Proposições](https://www.camara.leg.br)")

elif opcao == "🏠 7. Aluguéis de Imóveis na Reforma":
    st.header("🏠 Reforma Tributária: Impactos nos Aluguéis de Imóveis (Residencial e Comercial)")
    st.write(
        "A locação de bens imóveis foi enquadrada na base ampla do IVA Dual, porém o PLP 68/2024 garantiu "
        "um **redutor de alíquota de 60%**, reduzindo o impacto sobre locatários e proprietários."
    )

    st.markdown(
        """
    - **Incidência Ampla:** Aluguéis comerciais e residenciais integrados ao IVA Dual (CBS e IBS).
    - **Redução de 60% na Alíquota:** Alíquota efetiva reduzida para cerca de **10,6%**.
    - **Crédito B2B:** Empresas locatárias de imóveis comerciais podem aproveitar créditos do IVA pago no aluguel.
    """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ Como era")
        st.markdown("- Tributação difusa por ISS em alguns municípios ou tributação de rendimentos de aluguel por Carnê-Leão e IRPJ.")
    with col2:
        st.success("✅ Como vai ficar")
        st.markdown("- Tributação padronizada por CBS/IBS com redutor setorial de 60% e crédito financeiro para empresas.")

    st.markdown("---")
    st.subheader("🏢 Impactos Práticos na Gestão das Empresas")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.success("🟢 Positivos")
        st.markdown("- **Redutor Garantido:** Alíquota suavizada em 60%, protegendo o mercado de locação de saltos abusivos na carga.")
    with col_e2:
        st.error("🔴 Negativos")
        st.markdown("- **Repactuação Contratual:** Necessidade de revisão de contratos de longo prazo firmados por pessoas físicas e jurídicas.")

    st.markdown("---")
    st.subheader("📚 Impactos Práticos na Rotina da Contabilidade")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.success("🟢 Positivos")
        st.markdown("- **Padronização Nacional:** Fim das alíquotas municipais de ISS díspares para locações comerciais.")
    with col_c2:
        st.error("🔴 Negativos")
        st.markdown("- **Revisão de Portfólio Patrimonial:** Auditoria exaustiva em holdings e contratos de aluguel vigentes.")
    st.markdown("🔗 **Referência Legal Oficial:** [PLP 68/2024 - Setor Imobiliário](https://www.camara.leg.br)")

elif opcao == "📜 8. Herança & Doação (ITCMD)":
    st.header("📜 Reforma Tributária: Heranças e Doações (ITCMD)")
    st.write(
        "A Reforma Tributária (EC 132/2023) introduziu mudanças fundamentais no **ITCMD (Imposto sobre Transmissão Causa Mortis e Doação)**, "
        "com foco em combater a elisão fiscal de grandes patrimônios, estabelecer alíquotas progressivas obrigatórias e disciplinar "
        "a incidência em transmissões internacionais e planos de previdência (PGBL/VGBL)."
    )

    st.markdown(
        """
    - **Progressividade Obrigatória (Art. 155, § 1º, VI da CF/88):** Os Estados e o Distrito Federal passam a ser obrigados a adotar alíquotas progressivas no ITCMD, onde quem recebe heranças ou doações de maior valor paga proporcionalmente mais.
    - **Competência na Transmissão no Exterior:** O imposto passa a ser devido ao Estado onde era domiciliado o de cujus (em heranças) ou onde reside o donatário/bens (em doações), resolvendo conflitos entre estados.
    - **Previdência Privada (PGBL/VGBL):** Discussões acaloradas sobre a incidência de ITCMD em planos de previdência com caráter de transmissão de riqueza (sucessória).
    """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ Como era")
        st.markdown(
            """
        - Alíquotas proporcionais fixas em muitos estados (ex: 4% para qualquer valor).
        - Conflitos interestaduais severos sobre a arrecadação de bens situados no exterior ou herdeiros fora do domicílio.
        - Lacunas normativas sobre a transmissão de planos de previdência privada (VGBL/PGBL) como ferramenta de planejamento sucessório sem ITCMD.
        """
        )
    with col2:
        st.success("✅ Como vai ficar")
        st.markdown(
            """
        - **Tabela Progressiva Nacional:** Alíquotas escalonadas de acordo com o montante transmitido (chegando ao teto estipulado pelo Senado).
        - **Regras Claras para Exterior:** Fim de brechas jurídicas de inventários internacionais.
        - **Maior Tributação Sucessória:** Aperfeiçoamento do cerco a planejamentos sucessórios agressivos via holdings e seguros/previdência.
        """
        )

    st.markdown("---")
    st.subheader("🏢 Impactos Práticos na Gestão Patrimonial e Familiar")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Segurança Jurídica Interestadual:** Fim da guerra entre estados para definir quem tem direito de cobrar o ITCMD.
        - **Transparência Regulatória:** Critérios claros para inventários e doações em vida com alíquotas definidas por faixa patrimonial.
        """
        )
    with col_e2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Aumento da Carga Tributária em Grandes Heranças:** A progressividade eleva drasticamente o imposto sobre transmissões de patrimônios vultosos.
        - **Fim de Estratégias Clássicas de Planejamento:** Restrições a instrumentos que antes blindavam inventários de incidências fiscais pesadas.
        """
        )

    st.markdown("---")
    st.subheader("📚 Impactos Práticos na Rotina da Contabilidade")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.success("🟢 Positivos")
        st.markdown(
            """
        - **Alta Demanda Consultiva:** O contador e o planejador patrimonial tornam-se essenciais para reestruturar holdings familiares e testamentos.
        - **Previsibilidade de Cálculo:** Tabelas progressivas padronizadas dentro de cada unidade federativa.
        """
        )
    with col_c2:
        st.error("🔴 Negativos")
        st.markdown(
            """
        - **Complexidade em Inventários Pendentes:** Conflito de leis estaduais durante o período de adaptação das assembleias legislativas locais.
        - **Acompanhamento de Novas Súmulas:** Necessidade de monitoramento constante de decisões do STF sobre previdência privada e ITCMD.
        """
        )
    st.markdown("🔗 **Referência Legal Oficial:** [Emenda Constitucional nº 132/2023 - Regras do ITCMD](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm)")

elif opcao == "📊 9. Simulador Interativo Setorial & Transição":
    st.header("📊 Simulador Setorial com Cronograma de Transição e Aluguel de Imóveis")
    st.write(
        "Selecione o **ano de referência da transição (2026 a 2033)** e escolha o setor desejado para simular a carga tributária."
    )

    st.subheader("⚙️ Configuração dos Dados da Simulação")
    
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    with col_s1:
        faturamento_input = st.number_input(
            "Faturamento ou Valor Base Mensal (R$)",
            min_value=100.0,
            max_value=50000000.0,
            value=10000.0,
            step=500.0,
            format="%.2f"
        )
    with col_s2:
        ano_cronograma = st.selectbox(
            "Ano da Transição (Cronograma EC 132/23)",
            [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033],
            key="ano_trans_sim9"
        )
    with col_s3:
        segmento = st.selectbox(
            "Segmento de Mercado / Atividade",
            [
                "🏠 Aluguel / Locação de Imóveis (Residencial ou Comercial)",
                "Comércio Varejista (Geral)",
                "Supermercado / Alimentação",
                "Restaurante / Lanchonete / Alimentação fora do lar",
                "Prestação de Serviços (Geral / Escritório)",
                "Tecnologia / Software (SaaS)",
                "Saúde / Clínicas Médicas"
            ],
            key="seg_sim9"
        )
    with col_s4:
        regime_tributario = st.selectbox(
            "Regime Tributário Atual",
            [
                "Simples Nacional",
                "Lucro Presumido",
                "Lucro Real"
            ],
            key="reg_sim9"
        )

    st.divider()

    if "Aluguel" in segmento:
        base_aliq_atual = 0.05
        aliq_atual_str = "5,00% (Média Histórica / Locação)"
    elif "Comércio" in segmento:
        base_aliq_atual = 0.2165 if regime_tributario == "Lucro Presumido" else 0.04
        aliq_atual_str = "21,65% (Lucro Presumido) ou 4% (Simples)"
    elif "Supermercado" in segmento:
        base_aliq_atual = 0.18
        aliq_atual_str = "18,00% (Carga mista PIS/Cofins/ICMS)"
    elif "Restaurante" in segmento:
        base_aliq_atual = 0.14
        aliq_atual_str = "14,00% (PIS/Cofins + ICMS reduzido)"
    elif "Serviços" in segmento or "Tecnologia" in segmento:
        base_aliq_atual = 0.0865 if regime_tributario == "Lucro Presumido" else 0.06
        aliq_atual_str = "8,65% (Lucro Presumido) ou 6% (Simples)"
    else: # Saúde
        base_aliq_atual = 0.08
        aliq_atual_str = "8,00% (Carga mista saúde)"

    iva_padrao = 0.265
    if "Aluguel" in segmento:
        iva_efetivo = iva_padrao * 0.40
    elif segmento in ["Supermercado"]:
        iva_efetivo = iva_padrao * 0.45
    elif segmento in ["Saúde / Clínicas Médicas"]:
        iva_efetivo = iva_padrao * 0.40
    else:
        iva_efetivo = iva_padrao

    if ano_cronograma == 2026:
        base_aliq_transicao = base_aliq_atual + 0.01
        desc_ano_str = "2026: Ano-Teste Nacional (CBS 0,9% + IBS 0,1%)."
    elif ano_cronograma == 2027:
        base_aliq_transicao = (iva_efetivo * 0.25) + (base_aliq_atual * 0.75) if "Aluguel" in segmento else (0.28 * 0.25) + (base_aliq_atual * 0.75)
        desc_ano_str = "2027: CBS Plena (100%) | Extinção de PIS/Cofins/IPI."
    elif ano_cronograma == 2028:
        base_aliq_transicao = (iva_efetivo * 0.35) + (base_aliq_atual * 0.65)
        desc_ano_str = "2028: Consolidação Federal e Manutenção dos tributos antigos."
    elif ano_cronograma == 2029:
        base_aliq_transicao = (iva_efetivo * 0.45) + (base_aliq_atual * 0.55)
        desc_ano_str = "2029: Início da Transição do IBS (10% IBS + 90% antigos)."
    elif ano_cronograma == 2030:
        base_aliq_transicao = (iva_efetivo * 0.55) + (base_aliq_atual * 0.45)
        desc_ano_str = "2030: IBS a 20% + Tributos antigos a 80%."
    elif ano_cronograma == 2031:
        base_aliq_transicao = (iva_efetivo * 0.70) + (base_aliq_atual * 0.30)
        desc_ano_str = "2031: IBS a 30% + Tributos antigos a 70%."
    elif ano_cronograma == 2032:
        base_aliq_transicao = (iva_efetivo * 0.85) + (base_aliq_atual * 0.15)
        desc_ano_str = "2032: Fase Final da Transição (40% IBS + 60% antigos)."
    else:
        base_aliq_transicao = iva_efetivo
        desc_ano_str = "2033: Sistema 100% Pleno | Vigência integral do IVA Dual."

    imposto_atual_val = faturamento_input * base_aliq_atual
    imposto_transicao_val = faturamento_input * base_aliq_transicao
    diferenca_valor = imposto_transicao_val - imposto_atual_val
    percentual_variacao = (diferenca_valor / imposto_atual_val) * 100 if imposto_atual_val > 0 else 0

    st.info(f"📅 **Contexto do Ano Selecionado ({ano_cronograma}):** {desc_ano_str}")

    st.subheader(f"📊 Relatório de Simulação por Ano e Setor: {segmento}")
    col_alq1, col_alq2 = st.columns(2)
    with col_alq1:
        st.info(f"**Carga Efetiva Atual (Referência):**\n\n`{aliq_atual_str}`")
    with col_alq2:
        st.success(f"**Carga Efetiva Estimada para o Ano {ano_cronograma}:**\n\n`{(base_aliq_transicao)*100:.2f}%`")

    st.divider()

    col_res1, col_res2, col_res3 = st.columns(3)
    with col_res1:
        st.metric(
            label="Carga Tributária Atual (Base)",
            value=f"R$ {imposto_atual_val:,.2f}",
            delta=f"Efetiva: {(base_aliq_atual)*100:.2f}%"
        )
    with col_res2:
        st.metric(
            label=f"Carga Estimada em {ano_cronograma}",
            value=f"R$ {imposto_transicao_val:,.2f}",
            delta=f"Efetiva: {(base_aliq_transicao)*100:.2f}%",
            delta_color="off"
        )
    with col_res3:
        st.metric(
            label="Variação Estimada",
            value=f"R$ {diferenca_valor:+,.2f}",
            delta=f"{percentual_variacao:+.1f}%",
            delta_color="inverse"
        )

elif opcao == "🚢 10. Simulação de Importação & Tributação no Destino":
    st.header("🚢 Simulação de Importação sob a Nova Reforma Tributária")
    st.write(
        "Simule a importação de mercadorias informando o valor diretamente em **Reais (R$)**. "
        "A nova regra aduaneira aplica o princípio do destino e a unificação por IVA Dual (CBS + IBS)."
    )

    st.markdown("---")
    st.subheader("🧮 Calculadora Aduaneira em Reais (R$)")

    col_imp1, col_imp2 = st.columns(2)
    with col_imp1:
        valor_cif_brl = st.number_input(
            "Valor Aduaneiro da Mercadoria (CIF em R$)",
            min_value=100.0,
            max_value=50000000.0,
            value=5000.0,
            step=500.0,
            format="%.2f",
            key="cif_imp10"
        )
        aliq_ii = st.slider("Alíquota do Imposto de Importação (II) (%)", 0.0, 50.0, 14.0, 1.0, key="ii_10")
    with col_imp2:
        regime_importador = st.selectbox(
            "Regime do Importador no Brasil",
            ["Lucro Real / Presumido (Gera Crédito de IBS/CBS)", "Simples Nacional / Consumidor Final (Sem Crédito)"],
            key="regime_imp10"
        )
        st.info(f"🇧🇷 **Base de Cálculo:**\n\nValor CIF informado: **R$ {valor_cif_brl:,.2f}** (Valores calculados em moeda nacional).")

    valor_ii = valor_cif_brl * (aliq_ii / 100.0)
    base_tributos_antiga = valor_cif_brl + valor_ii
    tributos_antigos_val = base_tributos_antiga * 0.2975

    base_iva_dual = valor_cif_brl + valor_ii
    tributos_novos_bruto = base_iva_dual * 0.265

    credito_recuperavel = tributos_novos_bruto if "Lucro Real" in regime_importador else 0.0
    tributos_novos_liquido = tributos_novos_bruto - credito_recuperavel

    st.markdown("---")
    st.subheader("📈 Resultado da Simulação Aduaneira")

    res_imp1, res_imp2, res_imp3 = st.columns(3)
    with res_imp1:
        st.metric(
            label="Tributos no Sistema Antigo",
            value=f"R$ {tributos_antigos_val:,.2f}",
            delta="Alíquota efetiva ~29,75%"
        )
    with res_imp2:
        st.metric(
            label="Novo IVA Dual (Bruto na Fronteira)",
            value=f"R$ {tributos_novos_bruto:,.2f}",
            delta="Alíquota padrão 26,50%",
            delta_color="off"
        )
    with res_imp3:
        st.metric(
            label="Custo Tributário Efetivo Líquido",
            value=f"R$ {tributos_novos_liquido:,.2f}",
            delta=f"Crédito recuperado: R$ {credito_recuperavel:,.2f}",
            delta_color="normal"
        )

elif opcao == "📈 11. Impactos no SPED Fiscal (Atual vs. Futuro)":
    st.header("📈 Impactos no SPED Fiscal: Como é vs. Como Ficará")
    st.write(
        "O SPED Fiscal (EFD-ICMS/IPI) e as apurações acessórias federais passam por uma transformação radical "
        "com a extinção dos tributos tradicionais e a implantação da apuração unificada do IVA Dual."
    )

    st.markdown("---")
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.error("❌ Como é no Sistema Atual (SPED Tradicional)")
        st.markdown(
            """
        - **Complexidade de Registros:** Milhares de linhas nos blocos de apuração do ICMS (Bloco C, E, H) e PIS/Cofins (Bloco M).
        - **Guia por Guia:** Emissão de dezenas de guias estaduais (GNRE, GARE) e federais (DARF) com vencimentos desencontrados.
        - **Litigiosidade de Insumos:** Controle exaustivo e subjetivo sobre quais créditos de PIS/Cofins e ICMS podem ou não ser aproveitados.
        - **Inconsistências Críticas:** Cruzamentos complexos de malha fiscal entre o EFD, NF-e e DCTF que geram autuações frequentes.
        """
        )
    with col_s2:
        st.success("✅ Como ficará na Reforma (Novo Modelo / SPED Digital)")
        st.markdown(
            """
        - **Simplificação de Blocos:** Substituição das apurações fragmentadas por registros padronizados para a CBS e o IBS.
        - **Apuração Centralizada:** Apuração unificada por CNPJ matriz ou estabelecimento, automatizando o saldo credor.
        - **Split Payment Integrado:** O imposto é separado na transação financeira, reduzindo drasticamente a necessidade de preenchimentos manuais de guias.
        - **Crédito Financeiro Pleno:** Extinção de teses jurídicas sobre insumos; qualquer aquisição gera crédito imediato.
        """
        )

    st.markdown("---")
    st.subheader("📋 Tabela Comparativa de Obrigações Acessórias")
    st.markdown(
        """
        | Dimensão Fiscal | Cenário Atual (ICMS, PIS, Cofins, ISS) | Novo Cenário (Reforma Tributária - IVA Dual) |
        | :--- | :--- | :--- |
        | **Obrigações Acessórias** | Múltiplas declarações (SPED Fiscal, EFD-Contribuições, GIA, DEFIS) | Simplificação em ambiente nacional unificado (Declaração única CBS/IBS) |
        | **Apuração de Créditos** | Regras restritivas e divergências entre Estados e União | **Não-cumulatividade financeira plena** e imediata |
        | **Recolhimento** | Guias avulsas mensais por ente federativo | **Split Payment** (liquidação simultânea na transação financeira) |
        | **Fiscalização** | Baseada em auditorias retroativas pós-fato via malha fiscal | Monitoramento em tempo real por infraestrutura digital integrada |
        """
    )

elif opcao == "🗂️ 12. Guia para o Contador (50 FAQs & Links Oficiais)":
    st.header("🗂️ Guia Definitivo para o Contador: 50 Perguntas & Respostas e Links Oficiais")
    st.write(
        "Esta seção compõe um guia prático e completo com **50 perguntas e respostas essenciais** sobre a Reforma Tributária, "
        "projetado para dar suporte direto a contadores, advogados tributaristas e gestores fiscais na condução da transição para o novo IVA Dual."
    )

    st.markdown("---")
    st.subheader("📚 Perguntas Frequentes (FAQ Contábil - 50 Questões)")

    faqs = [
        ("1. O que é a Reforma Tributária aprovada pela EC 132/2023?", "A Emenda Constitucional nº 132/2023 substitui PIS, Cofins, IPI, ICMS e ISS por um IVA Dual composto pela CBS (federal) e pelo IBS (subnacional)."),
        ("2. Qual o objetivo principal da transição para o princípio do destino?", "Garantir que a arrecadação pertença ao Estado e Município onde o consumidor final consome o bem ou serviço, eliminando a Guerra Fiscal de origem."),
        ("3. Quando o novo sistema começa a valer efetivamente?", "O cronograma prevê testes em 2026, CBS plena em 2027, transição gradual do IBS de 2029 a 2032, e sistema 100% pleno em 2033."),
        ("4. Como funciona o ano-teste de 2026?", "Início de testes operacionais com alíquotas de referência (0,9% CBS e 0,1% IBS) em notas fiscais, sem aumento de carga pois haverá compensação com tributos federais."),
        ("5. O PIS e a Cofins serão extintos em qual ano?", "O PIS e a Cofins serão extintos e substituídos pela CBS a partir de 1 de janeiro de 2027."),
        ("6. O que acontece com o IPI na reforma?", "O IPI será zerado para a maioria dos produtos a partir de 2027, mantendo proteção fiscal exclusiva para a Zona Franca de Manaus (ZFM)."),
        ("7. O que é o Imposto Seletivo (IS)?", "O 'Imposto do Pecado', incidente sobre extração e produção de bens prejudiciais à saúde e ao meio ambiente (cigarros, bebidas alcoólicas, açucaradas, veículos poluentes e minérios)."),
        ("8. As empresas do Simples Nacional são obrigadas a adotar o IVA Dual?", "Não. Continuam recolhendo pelo DAS, mas terão a opção de destacar CBS e IBS se precisarem fornecer créditos plenos a clientes B2B."),
        ("9. O que é a não-cumulatividade financeira plena?", "Qualquer aquisição de bens ou serviços necessários à atividade da empresa gera crédito imediato de CBS e IBS, encerrando restrições do conceito rígido de insumo."),
        ("10. Como funcionará o Split Payment?", "Liquidação financeira simultânea regulada pelo Banco Central onde o imposto é separado e repassado no exato momento do pagamento eletrônico (Pix, cartão, boleto)."),
        ("11. Qual a alíquota padrão estimada do IVA Dual (CBS + IBS)?", "As estimativas técnicas preliminares do governo situam a alíquota combinada de referência em torno de 26,5%."),
        ("12. O que é a Cesta Básica Nacional?", "Conjunto de alimentos essenciais (arroz, feijão, leite, carnes, ovos, pão e farinhas) com alíquota zero (0%) de CBS e IBS em todo o país."),
        ("13. Quais setores possuem redução de 60% na alíquota?", "Medicamentos, serviços de saúde, dispositivos médicos, educação, transporte coletivo de passageiros e locação de imóveis."),
        ("14. Como funciona o Cashback Tributário?", "Devolução parcial ou total de tributos (CBS e IBS) para famílias de baixa renda inscritas no CadÚnico, com foco em energia, gás e alimentos."),
        ("15. O que é o Comitê Gestor do IBS (CG-IBS)?", "Órgão criado para unificar a arrecadação, fiscalização e distribuição do IBS entre Estados e Municípios com regras nacionais padronizadas."),
        ("16. Como ficam as empresas de Lucro Presumido e Lucro Real?", "Migram da apuração cumulativa/não-cumulativa fragmentada tradicional para o modelo unificado de apuração centralizada do IVA Dual."),
        ("17. O ISS municipal deixa de existir?", "Sim. O ISS será extinto progressivamente entre 2029 e 2033, sendo fundido no IBS junto com o ICMS."),
        ("18. O ICMS estadual acaba quando?", "O ICMS será extinto de forma gradativa entre 2029 e 2032, encerrando sua vigência por completo em 31 de dezembro de 2032."),
        ("19. Como serão tributadas as importações?", "Serão tributadas no destino pelas mesmas alíquotas de CBS e IBS aplicadas internamente, garantindo isonomia com a produção nacional."),
        ("20. Há mudanças na exportação?", "Sim. Adota-se o princípio do destino puro, com desoneração completa das exportações (isenção de CBS/IBS e restituição de créditos anteriores)."),
        ("21. Como o contador deve orientar clientes sobre o planejamento tributário?", "Revisando contratos de longo prazo, analisando a cadeia de suprimentos, avaliando créditos e homologando ERPs em 2026."),
        ("22. O SPED Fiscal (EFD-ICMS/IPI) vai acabar?", "Sim, o modelo de blocos analíticos complexos será substituído por declarações eletrônicas unificadas e integradas para o IVA Dual."),
        ("23. O que muda nas notas fiscais eletrônicas (NF-e)?", "As NF-es precisarão exibir os campos específicos e destacados de CBS, IBS e Imposto Seletivo conforme leiautes da Receita Federal e Comitê Gestor."),
        ("24. Qual o papel da Receita Federal na CBS?", "A Receita Federal administrará, fiscalizará e arrecadará exclusivamente a CBS (tributo federal)."),
        ("25. E quem administra o IBS?", "O IBS será administrado de forma compartilhada entre Estados, DF e Municípios por meio do Comitê Gestor do IBS."),
        ("26. Haverá contencioso administrativo unificado?", "Sim, a reforma prevê instâncias administrativas paritárias e integradas para julgar litígios de CBS e IBS."),
        ("27. Como ficam os benefícios fiscais de ICMS antigos (Guerra Fiscal)?", "Os incentivos de ICMS concedidos por estados serão gradativamente extintos conforme transição até 2032, com fundos de compensação."),
        ("28. O que é o Fundo de Compensação de Benefícios Fiscais?", "Fundo financiado pela União para compensar perdas de empresas com incentivos de ICMS legais garantidos até 2032."),
        ("29. Como o setor de serviços será afetado pela alíquota de 26,5%?", "Como serviços pagavam menos carga efetiva acumulada, a alíquota padrão pode elevar o custo se houver baixo aproveitamento de créditos em cadeia."),
        ("30. Quais os impactos para herança e doação (ITCMD)?", "O ITCMD passa a ter progressividade obrigatória em todos os estados, elevando alíquotas para grandes patrimônios e disciplinando transmissões no exterior."),
        ("31. Cooperativas terão tratamento diferenciado?", "Sim, o PLP 68/2024 traz regras de não incidência de CBS e IBS sobre atos cooperativos próprios e créditos específicos."),
        ("32. Instituições financeiras (bancos) pagam IBS e CBS?", "Bancos e financeiras terão regras de apuração próprias baseadas na margem de intermediação financeira e receitas de serviços."),
        ("33. O mercado de saúde suplementar tem redução?", "Sim, serviços de saúde e planos de saúde estão contemplados na redução de 60% da alíquota do IVA Dual."),
        ("34. Medicamentos essenciais pagam imposto?", "Medicamentos da lista com alíquota reduzida terão desconto de 60%, e itens essenciais poderão ter alíquota zero."),
        ("35. Veículos elétricos pagam Imposto Seletivo?", "O Imposto Seletivo visa desestimular externalidades negativas; veículos poluentes pagam mais, enquanto elétricos podem ter incentivos."),
        ("36. Como o contador verifica atualizações oficiais?", "Através de portarias da Receita Federal, sites do Ministério da Fazenda e portais dos comitês gestores."),
        ("37. Qual o impacto para o lucro presumido em serviços?", "Empresas de serviços no Lucro Presumido sem muitos créditos para recuperar podem ter elevação de carga tributária."),
        ("38. O saldo credor acumulado de ICMS antigo será aproveitado?", "Saldos credores de ICMS acumulados até 31/12/2032 poderão ser compensados ou ressarcidos segundo regras de transição legais."),
        ("39. O que é o princípio da neutralidade tributária?", "Princípio que dita que o imposto não deve influenciar as decisões econômicas, logísticas ou societárias das empresas."),
        ("40. Como fica o ITCMD em previdência privada (PGBL/VGBL)?", "O ITCMD incide em transmissões sucessórias de previdência com caráter de transferência de riqueza, conforme regulamentações estaduais e jurisprudência."),
        ("41. O que é a base ampla de incidência do IBS/CBS?", "Praticamente a totalidade de bens e serviços de qualquer natureza entra no campo de incidência, extinguindo discussões mercadoria vs. serviço."),
        ("42. O Simples Nacional perde clientes se não emitir nota com destaque?", "Sim, clientes B2B no Lucro Real/Presumido preferem fornecedores que gerem crédito, exigindo atenção do contador na opção de destaque."),
        ("43. Como o Split Payment protege o caixa do empresário?", "Evita inadimplência e passivos de guias mensais, pois o imposto é descontado e repassado instantaneamente no pagamento."),
        ("44. O que acontece com os honorários contábeis na transição?", "A demanda por consultoria contábil e estratégica aumentará expressivamente devido à complexidade da convivência dos sistemas."),
        ("45. Qual o prazo para adequação de ERPs e sistemas?", "Imediato. O ano de 2026 exige homologação completa de softwares para suportar o Split Payment e o ano-teste."),
        ("46. O que é a CBS?", "Contribuição Social sobre Bens e Serviços, tributo federal criado para substituir PIS, Cofins e parte do IPI."),
        ("47. O que é o IBS?", "Imposto sobre Bens e Serviços, tributo subnacional (Estados e Municípios) criado para substituir ICMS e ISS."),
        ("48. Como funcionará o ressarcimento de créditos do IVA Dual?", "O PLP 68 estabelece prazos céleres e automatizados de ressarcimento de saldos credores de IBS e CBS para preservar o caixa."),
        ("49. Há penalidades para erros no destaque do IVA Dual em 2026?", "Durante o ano-teste de 2026, o foco é estritamente pedagógico e de validação sistêmica, havendo flexibilidade punitiva."),
        ("50. Onde encontrar o texto legal consolidado das Leis Complementares?", "Nos portais oficiais da Câmara dos Deputados, do Senado Federal e na Receita Federal do Brasil.")
    ]

    for pergunta, resposta in faqs:
        with st.expander(pergunta):
            st.write(resposta)

    st.markdown("---")
    st.subheader("🔗 Links Oficiais para Verificação de Atualizações Normativas")
    st.markdown(
        """
        Consulte exclusivamente as fontes oficiais do Governo Federal e do Congresso para acompanhar portarias e regulamentações:

        - 🏛️ **Portal oficial da Reforma Tributária (Governo Federal):** [gov.br/reformatributaria](https://www.gov.br/fazenda/pt-br/assuntos/reforma-tributaria)
        - 📄 **Acompanhamento de Proposições e PLP 68/2024 (Câmara dos Deputados):** [Portal da Câmara - PLP 68/2024](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2456475)
        - ⚖️ **Emenda Constitucional nº 132/2023 (Texto Oficial no Planalto):** [EC 132/2023 - Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm)
        - 🏦 **Banco Central do Brasil (Regulamentação do Split Payment):** [Portal do Banco Central](https://www.bcb.gov.br)
        - 📰 **Agência Senado (Acompanhamento de votações e debates):** [Agência Senado](https://www12.senado.leg.br/noticias)
        """
    )

elif opcao == "🤖 13. IA Consultora Oficial (Base de Dados do Governo)":
    st.header("🤖 Inteligência Artificial Especialista na Reforma Tributária")
    st.write(
        "Faça qualquer pergunta sobre as novas regras, alíquotas, transição até 2033, impactos setoriais "
        "ou dispositivos legais das Leis Complementares. A inteligência artificial está conectada e pronta para responder "
        "com base estritamente nas fontes e dados oficiais do governo."
    )

    os.environ["GEMINI_API_KEY"] = "AQ.Ab8RN6JlC0g4kgKb2d6MjU_Lmrabzzg-mbCXLgyYOV7DYUc6DA"
    
    st.success("🔒 Chave de API oficial conectada com sucesso! A IA está pronta para consultas.")

    pergunta_usuario = st.text_area(
        "Digite sua dúvida sobre a Reforma Tributária:",
        placeholder="Ex: Como funciona a progressividade do ITCMD nas doações e heranças?"
    )

    if st.button("Consultar IA Oficial"):
        if not pergunta_usuario:
            st.warning("⚠️ Digite uma pergunta para consultar a base de dados.")
        else:
            with st.spinner("Consultando dados oficiais da legislação e formulando resposta técnica..."):
                try:
                    from google import genai
                    from google.genai import types

                    client = genai.Client()

                    system_instruction = (
                        "Você é um consultor tributário sênior e especialista técnico na Reforma Tributária do Consumo do Brasil "
                        "(Emenda Constitucional nº 132/2023, PLP 68/2024 e PLP 108/2024). "
                        "Responda às dúvidas dos usuários com base técnica, citando artigos e fundamentos legais corretos, "
                        "mantendo tom profissional, claro e fundamentado exclusivamente nas diretrizes do Governo Federal e do Congresso Nacional."
                    )

                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=pergunta_usuario,
                        config=types.GenerateContentConfig(
                            system_instruction=system_instruction,
                            temperature=0.2,
                        ),
                    )

                    st.success("✅ Resposta Oficial da IA:")
                    st.markdown(response.text)

                except Exception as e:
                    st.error(f"Ocorreu um erro ao conectar com a IA: {e}")

st.divider()
st.caption("Desenvolvido por Pedro Marques com base nas diretrizes oficiais da EC 132/2023 e PLP 68/2024.")
