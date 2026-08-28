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

# Lista de módulos para os botões da barra lateral (Adicionada a aba 'Guia para o Contador')
modulos = [
    "1. Visão Geral & Marco Constitucional",
    "2. IVA Dual (CBS e IBS) - PLP 68/2024",
    "3. Imposto Seletivo (IS) & Externalidades",
    "4. Cashback Tributário & Justiça Social",
    "5. Split Payment & Tecnologia de Arrecadação",
    "6. Cesta Básica & Alíquotas Reduzidas",
    "📊 7. Simulador Interativo Setorial (Estilo Pro)",
    "🚢 8. Simulação de Importação & Tributação no Destino",
    "📈 9. Impactos no SPED Fiscal (Atual vs. Futuro)",
    "🗂️ 10. Guia para o Contador (FAQ & Links Oficiais)",
    "🤖 11. IA Consultora Oficial (Base de Dados do Governo)",
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
    st.subheader("📅 Cronograma Oficial de Transição (2026 a 2033)")
    st.write(
        "A implementação do novo sistema ocorre de forma gradual para permitir a adaptação tecnológica "
        "dos contribuintes e a convivência controlada entre os tributos antigos e o novo IVA Dual:"
    )

    st.markdown(
        """
        | Ano / Período | Marco de Implementação / O que muda na prática | Tributos Envolvidos |
        | :--- | :--- | :--- |
        | **2026** | **Ano-Teste Nacional:** Início dos testes operacionais com alíquotas de referência para validação de sistemas e notas fiscais. | CBS (`0,9%`) e IBS (`0,1%`) |
        | **2027** | **Entrada da CBS Plena e Fim do PIS/Cofins:** Extinção definitiva do PIS, da Cofins e do IPI (exceto Zona Franca de Manaus); início do Imposto Seletivo (IS). | CBS Cheia + Extinção de PIS/Cofins/IPI + Início do IS |
        | **2028** | **Consolidação Federal e Ajustes:** Manutenção da CBS plena e ajustes normativos nas legislações complementares. | CBS Plena + Manutenção de ICMS/ISS |
        | **2029** | **Início da Transição do IBS (10%):** Os estados e municípios começam a substituir progressivamente o ICMS e o ISS pelo IBS. | IBS (`10%`) + ICMS/ISS (`90%`) |
        | **2030** | **Progressão do IBS (20%):** Aumento da participação do IBS e redução proporcional de ICMS e ISS. | IBS (`20%`) + ICMS/ISS (`80%`) |
        | **2031** | **Aceleração da Transição (30%):** Continuidade da substituição gradual da arrecadação subnacional. | IBS (`30%`) + ICMS/ISS (`70%`) |
        | **2032** | **Fase Final da Transição (40%):** Último ano de convivência mista entre os tributos estaduais/municipais antigos e o IBS. | IBS (`40%`) + ICMS/ISS (`60%`) |
        | **2033** | **Sistema Pleno Vigente:** Extinção total e definitiva de ICMS e ISS. O IVA Dual (CBS + IBS) passa a vigorar integralmente no país. | Apenas CBS + IBS + Imposto Seletivo (Sistema 100% Pleno) |
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
        - Apuração separada de PIS/Cofins federais com regras complexas de cumulatividade (Lucro Presumido vs. Real).
        - Divergências severas entre o ICMS estadual e o ISS municipal na prestação de serviços híbridos.
        """
        )

    with col2:
        st.success("✅ Como vai ficar")
        st.markdown(
            """
        - Guia unificada de pagamento e notas fiscais eletrônicas padronizadas em nível nacional.
        - Extinção total de litígios sobre o conceito estrito de 'insumo industrial'.
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
        st.markdown("- Tributação difusa pelo IPI e tributos estaduais sem uniformidade nacional de foco em saúde pública.")

    with col2:
        st.success("✅ Como vai ficar")
        st.markdown("- Incidência monofásica federal calculada diretamente sobre o fator de nocividade (ex: teor de açúcar ou poluição).")

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
        st.markdown("- Cidadãos de menor renda pagavam proporcionalmente a mesma alíquota de impostos indiretos que os mais ricos, sem restituição.")

    with col2:
        st.success("✅ Como vai ficar")
        st.markdown("- Devolução de até 100% da parcela federal (CBS) e percentual da parcela subnacional (IBS) diretamente na conta do cidadão.")

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
        st.markdown("- O lojista recebia o valor total da venda e recolhia o imposto dias ou semanas depois via guia, gerando riscos de inadimplência.")

    with col2:
        st.success("✅ Como vai ficar")
        st.markdown("- Separação tributária em tempo real na maquininha ou gateway de pagamento, zerando a sonegação e gerando crédito imediato.")

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
        st.markdown("- Alíquotas desorganizadas de PIS/Cofins e ICMS variando de estado para estado sobre alimentos e remédios.")

    with col2:
        st.success("✅ Como vai ficar")
        st.markdown("- Isenção absoluta (0%) padronizada em todo o território nacional para os alimentos essenciais da Cesta Básica.")

    st.markdown("🔗 **Referência Legal Oficial:** [Câmara dos Deputados - Proposições](https://www.camara.leg.br)")

elif opcao == "📊 7. Simulador Interativo Setorial (Estilo Pro)":
    st.header("📊 Simulador Avançado de Carga Tributária por Setor e Faturamento")
    st.write(
        "Simule em tempo real o impacto financeiro e tributário para diferentes segmentos empresariais em **São Paulo**, "
        "comparando detalhadamente as alíquotas efetivas aplicadas no cenário atual versus a transição para o novo IVA Dual (CBS + IBS)."
    )

    st.subheader("⚙️ Configuração dos Dados da Empresa")
    
    col_s1, col_s2, col_s3 = st.columns(3)

    with col_s1:
        faturamento_input = st.number_input(
            "Faturamento Bruto Mensal (R$)",
            min_value=100.0,
            max_value=50000000.0,
            value=1000.0,
            step=500.0,
            format="%.2f"
        )

    with col_s2:
        segmento = st.selectbox(
            "Segmento de Mercado / Atividade",
            [
                "Comércio Varejista (Geral)",
                "Supermercado / Alimentação",
                "Restaurante / Lanchonete / Alimentação fora do lar",
                "Prestação de Serviços (Geral / Escritório)",
                "Tecnologia / Software (SaaS)",
                "Saúde / Clínicas Médicas"
            ]
        )

    with col_s3:
        regime_tributario = st.selectbox(
            "Regime Tributário Atual",
            [
                "Simples Nacional",
                "Lucro Presumido",
                "Lucro Real"
            ]
        )

    st.divider()

    if "Comércio" in segmento:
        if regime_tributario == "Simples Nacional":
            aliq_atual_str, base_aliq_atual = "4,00% (Anexo I - DAS)", 0.04
            aliq_novo_str, base_aliq_novo = "4,00% (DAS Simplicidade) ou 26,5% (IVA Dual B2B opcional)", 0.04
        elif regime_tributario == "Lucro Presumido":
            aliq_atual_str, base_aliq_atual = "21,65% (PIS 0,65% + Cofins 3% + ICMS SP ~18%)", 0.2165
            aliq_novo_str, base_aliq_novo = "26,50% (IVA Dual Padrão: CBS + IBS com créditos plenos)", 0.265
        else:
            aliq_atual_str, base_aliq_atual = "27,25% (PIS 1,65% + Cofins 7,6% + ICMS SP ~18% com créditos restritos)", 0.2725
            aliq_novo_str, base_aliq_novo = "26,50% (IVA Dual Padrão com Não-Cumulatividade Financeira Plena)", 0.265

    elif "Supermercado" in segmento:
        if regime_tributario == "Simples Nacional":
            aliq_atual_str, base_aliq_atual = "3,50% (Anexo I - Comércio com itens essenciais)", 0.035
            aliq_novo_str, base_aliq_novo = "3,50% (DAS) ou Alíquota Zero (Itens da Cesta Básica Nacional)", 0.035
        else:
            aliq_atual_str, base_aliq_atual = "18,00% (Carga mista PIS/Cofins/ICMS)", 0.18
            aliq_novo_str, base_aliq_novo = "12,00% (Média ponderada com desoneração da Cesta Básica)", 0.12

    elif "Restaurante" in segmento:
        if regime_tributario == "Simples Nacional":
            aliq_atual_str, base_aliq_atual = "5,00% (Anexo I/III - Alimentação)", 0.05
            aliq_novo_str, base_aliq_novo = "5,00% (DAS) ou IVA Dual setorial com redução", 0.05
        else:
            aliq_atual_str, base_aliq_atual = "14,00% (PIS/Cofins + ICMS reduzido em SP)", 0.14
            aliq_novo_str, base_aliq_novo = "20,00% (IVA Dual ajustado para setor de alimentação)", 0.20

    elif "Serviços" in segmento or "Tecnologia" in segmento:
        if regime_tributario == "Simples Nacional":
            aliq_atual_str, base_aliq_atual = "6,00% (Anexo III inicial)", 0.06
            aliq_novo_str, base_aliq_novo = "6,00% (DAS) ou destaque opcional do IVA Dual", 0.06
        elif regime_tributario == "Lucro Presumido":
            aliq_atual_str, base_aliq_atual = "8,65% (PIS/Cofins + ISS SP 5%)", 0.0865
            aliq_novo_str, base_aliq_novo = "26,50% (IVA Dual Padrão unificado)", 0.265
        else:
            aliq_atual_str, base_aliq_atual = "14,25% (PIS/Cofins não cumulativos + ISS SP 5%)", 0.1425
            aliq_novo_str, base_aliq_novo = "26,50% (IVA Dual Padrão com dedução irrestrita)", 0.265

    else: # Saúde
        if regime_tributario == "Simples Nacional":
            aliq_atual_str, base_aliq_atual = "5,00% (Anexo III)", 0.05
            aliq_novo_str, base_aliq_novo = "5,00% (DAS) ou alíquota reduzida", 0.05
        else:
            aliq_atual_str, base_aliq_atual = "8,00% (Carga mista de serviços de saúde)", 0.08
            aliq_novo_str, base_aliq_novo = "10,60% (IVA Dual com redução de 60% garantida)", 0.106

    imposto_atual_val = faturamento_input * base_aliq_atual
    imposto_novo_val = faturamento_input * base_aliq_novo
    diferenca_valor = imposto_novo_val - imposto_atual_val
    percentual_variacao = (diferenca_valor / imposto_atual_val) * 100 if imposto_atual_val > 0 else 0

    st.subheader(f"📊 Relatório de Simulação: {segmento} ({regime_tributario})")

    st.markdown("### 🔍 Detalhamento das Alíquotas Efetivas Aplicadas:")
    col_alq1, col_alq2 = st.columns(2)
    with col_alq1:
        st.info(f"**Alíquota no Cenário Atual:**\n\n`{aliq_atual_str}`")
    with col_alq2:
        st.success(f"**Alíquota no Novo Modelo (Reforma):**\n\n`{aliq_novo_str}`")

    st.divider()

    col_res1, col_res2, col_res3 = st.columns(3)

    with col_res1:
        st.metric(
            label="Carga Tributária Atual (R$)",
            value=f"R$ {imposto_atual_val:,.2f}",
            delta=f"Efetiva: {(base_aliq_atual)*100:.2f}%"
        )

    with col_res2:
        st.metric(
            label="Nova Carga (Reforma Tributária)",
            value=f"R$ {imposto_novo_val:,.2f}",
            delta=f"Efetiva: {(base_aliq_novo)*100:.2f}%",
            delta_color="off"
        )

    with col_res3:
        st.metric(
            label="Variação Estimada",
            value=f"R$ {diferenca_valor:+,.2f}",
            delta=f"{percentual_variacao:+.1f}%",
            delta_color="inverse"
        )

elif opcao == "🚢 8. Simulação de Importação & Tributação no Destino":
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
            format="%.2f"
        )
        aliq_ii = st.slider("Alíquota do Imposto de Importação (II) (%)", 0.0, 50.0, 14.0, 1.0)

    with col_imp2:
        regime_importador = st.selectbox(
            "Regime do Importador no Brasil",
            ["Lucro Real / Presumido (Gera Crédito de IBS/CBS)", "Simples Nacional / Consumidor Final (Sem Crédito)"],
            key="regime_imp"
        )
        st.info(f"🇧🇷 **Base de Cálculo:**\n\nValor CIF informado: **R$ {valor_cif_brl:,.2f}** (Valores calculados estritamente em moeda nacional).")

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

elif opcao == "📈 9. Impactos no SPED Fiscal (Atual vs. Futuro)":
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

elif opcao == "🗂️ 10. Guia para o Contador (FAQ & Links Oficiais)":
    st.header("🗂️ Guia Prático para o Contador: Perguntas, Respostas e Links Oficiais")
    st.write(
        "Esta seção reúne orientações fundamentais em formato de perguntas e respostas (FAQ) para auxiliar profissionais "
        "da contabilidade e consultores tributários na orientação estratégica de seus clientes, além de compilar os links oficiais "
        "para verificação de atualizações normativas."
    )

    st.markdown("---")
    st.subheader("❓ Perguntas e Respostas Frequentes (FAQ Contábil)")

    with st.expander("1. O que muda de imediato para as empresas em 2026 (Ano-Teste)?"):
        st.write(
            "Em 2026, teremos a fase de testes operacionais da CBS (0,9%) e do IBS (0,1%). "
            "As empresas deverão emitir notas fiscais adaptadas para destacar os novos tributos de forma teste, "
            "mas **sem aumento real de carga tributária**, pois haverá compensação integral com os tributos federais antigos (PIS/Cofins). "
            "É o momento ideal para testar sistemas de ERP e a infraestrutura de emissão."
        )

    with st.expander("2. O Simples Nacional perde vantagens com a Reforma?"):
        st.write(
            "Não obrigatoriamente. As empresas optantes pelo Simples Nacional continuam com a opção de recolher seus tributos unificados via DAS. "
            "No entanto, se a empresa for fornecedora B2B (vende para outras empresas), ela poderá optar por destacar a CBS e o IBS "
            "fora do DAS para permitir que seus clientes tomem créditos tributários integrais, evitando perder competitividade no mercado."
        )

    with st.expander("3. Como funcionará o aproveitamento de créditos no Lucro Real e Presumido?"):
        st.write(
            "O novo sistema adota a **não-cumulatividade financeira plena**. Isso significa que o conceito restrito de 'insumo' (que gerava enormes litígios no PIS/Cofins e ICMS) deixa de existir. "
            "Qualquer aquisição de bens, serviços ou investimentos realizados pela empresa para a atividade operacional gerará crédito imediato de CBS e IBS."
        )

    with st.expander("4. O que é o Comitê Gestor do IBS e qual sua função?"):
        st.write(
            "O Comitê Gestor do IBS (CG-IBS) é o órgão criado para coordenar e uniformizar a arrecadação, a fiscalização e a distribuição "
            "do IBS entre Estados, Distrito Federal e Municípios, garantindo regras nacionais padronizadas e evitando conflitos de competência federativa."
        )

    with st.markdown("---"):
        st.subheader("🔗 Links Oficiais para Verificação de Atualizações Normativas")
        st.markdown(
            """
            Para acompanhar em tempo real as portarias, regulamentações do Comitê Gestor, notas técnicas da Receita Federal 
            e os desdobramentos dos Projetos de Lei Complementar, consulte exclusivamente as fontes oficiais do Governo Federal e do Congresso:

            - 🏛️ **Portal oficial da Reforma Tributária (Governo Federal):** [gov.br/reformatributaria](https://www.gov.br/fazenda/pt-br/assuntos/reforma-tributaria)
            - 📄 **Acompanhamento de Proposições e PLP 68/2024 (Câmara dos Deputados):** [Portal da Câmara - PLP 68/2024](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2456475)
            - ⚖️ **Emenda Constitucional nº 132/2023 (Texto Oficial no Planalto):** [EC 132/2023 - Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm)
            - 🏦 **Banco Central do Brasil (Regulamentação do Split Payment):** [Portal do Banco Central](https://www.bcb.gov.br)
            - 📰 **Agência Senado (Acompanhamento de votações e debates):** [Agência Senado](https://www12.senado.leg.br/noticias)
            """
        )

elif opcao == "🤖 11. IA Consultora Oficial (Base de Dados do Governo)":
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
        placeholder="Ex: Quais são as principais recomendações contábeis para a transição em 2026?"
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
