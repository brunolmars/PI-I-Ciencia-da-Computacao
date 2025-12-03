<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Recursos - SGEF</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" />

    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap" rel="stylesheet" />

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" />

    <style>
        :root {
            --cor-primaria: #007bff;
            --cor-secundaria: #6c757d;
            --fundo-claro: #f8f9fa;
        }

        body {
            background-color: var(--fundo-claro);
            font-family: "Montserrat", sans-serif;
        }

        .navbar {
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .navbar-brand {
            font-weight: 900;
            color: var(--cor-primaria) !important;
            letter-spacing: 1px;
        }

        .nav-link {
            font-weight: 500;
            color: #343a40 !important;
        }

        .hero-section {
            padding: 80px 0;
            text-align: center;
            background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
            color: white;
        }

        .hero-section h1 {
            font-weight: 900;
            font-size: 3rem;
            margin-bottom: 20px;
        }

        .hero-section p {
            font-size: 1.2rem;
            margin-bottom: 30px;
            opacity: 0.9;
        }

        .cta-button {
            font-size: 1.5rem;
            padding: 20px 50px;
            font-weight: 700;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }

        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        }

        .calculator-section {
            padding: 60px 0;
        }

        .calculator-card {
            background: white;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            padding: 40px;
        }

        .calculator-card h2 {
            font-weight: 900;
            color: var(--cor-primaria);
            margin-bottom: 30px;
        }

        .form-label {
            font-weight: 600;
            color: #343a40;
        }

        .result-box {
            background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-top: 30px;
            text-align: center;
        }

        .result-box h3 {
            font-weight: 700;
            margin-bottom: 20px;
        }

        .result-value {
            font-size: 2.5rem;
            font-weight: 900;
            margin: 10px 0;
        }

        .result-detail {
            font-size: 1.2rem;
            opacity: 0.9;
            margin: 5px 0;
        }

        .btn-calculate {
            background: var(--cor-primaria);
            color: white;
            font-weight: 700;
            padding: 12px 40px;
            border: none;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .btn-calculate:hover {
            background: #0056b3;
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 123, 255, 0.3);
        }

        .input-group-text {
            background-color: var(--cor-primaria);
            color: white;
            font-weight: 600;
        }
    </style>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-white sticky-top">
        <div class="container">
            <a class="navbar-brand" href="index.html">SGEF</a>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menuNavbar"
                aria-controls="menuNavbar" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="menuNavbar">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li>
                        <a class="nav-link" href="../index.html">Início</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="recursos.php">Recursos</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="contato.html">Contato</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="../dashboard_Bruno.html">Dashboard</a>
                    </li>
                </ul>

                <div class="d-flex">
                    <a href="#" class="btn btn-outline-primary me-2">Entrar</a>
                    <a href="#" class="btn btn-primary">Cadastrar-se</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section with CTA Button -->
    <section class="hero-section">
        <div class="container">
            <h1>Descubra Seu Potencial de Investimento</h1>
            <p>Conheça seu perfil e tome decisões financeiras mais inteligentes</p>
            <a href="https://pt.quizur.com/quiz/perfil-de-investidor-VyM2" target="_blank"
                class="btn btn-light btn-lg cta-button">Descubra Seu Perfil de Investimento</a>
        </div>
    </section>

    <!-- Compound Interest Calculator -->
    <section class="calculator-section">
        <div class="container">
            <div class="calculator-card">
                <h2 class="text-center"><i class="bi bi-calculator me-2"></i>Calculadora de Juros Compostos</h2>
                <p class="text-center text-secondary mb-4">Simule o crescimento do seu investimento ao longo do tempo
                </p>

                <div class="row">
                    <div class="col-md-6">
                        <div class="mb-3">
                            <label for="valorInicial" class="form-label">Valor Inicial (R$)</label>
                            <div class="input-group">
                                <span class="input-group-text">R$</span>
                                <input type="text" class="form-control currency-input" id="valorInicial"
                                    placeholder="1.000,00" value="1.000,00">
                            </div>
                        </div>

                        <div class="mb-3">
                            <label for="aporteMensal" class="form-label">Aporte Mensal (R$)</label>
                            <div class="input-group">
                                <span class="input-group-text">R$</span>
                                <input type="text" class="form-control currency-input" id="aporteMensal"
                                    placeholder="500,00" value="500,00">
                            </div>
                        </div>

                        <div class="mb-3">
                            <label for="taxaJuros" class="form-label">Taxa de Juros Anual (%)</label>
                            <div class="input-group">
                                <input type="number" class="form-control" id="taxaJuros" placeholder="8.0" value="8"
                                    step="0.1" min="0">
                                <span class="input-group-text">%</span>
                            </div>
                        </div>

                        <div class="mb-3">
                            <label for="periodo" class="form-label">Período (anos)</label>
                            <input type="number" class="form-control" id="periodo" placeholder="10" value="10" step="1"
                                min="0">
                        </div>

                        <button class="btn btn-calculate w-100" onclick="calcularJurosCompostos()">
                            <i class="bi bi-graph-up me-2"></i>Calcular
                        </button>
                    </div>

                    <div class="col-md-6">
                        <div id="resultadoCalculadora" class="result-box" style="display: none;">
                            <h3><i class="bi bi-trophy me-2"></i>Resultado da Simulação</h3>
                            <div class="result-value" id="valorFinal">R$ 0,00</div>
                            <div class="result-detail">Valor Final</div>
                            <hr style="border-color: rgba(255,255,255,0.3); margin: 20px 0;">
                            <div class="row text-center">
                                <div class="col-6">
                                    <div class="result-detail" id="totalInvestido">R$ 0,00</div>
                                    <small>Total Investido</small>
                                </div>
                                <div class="col-6">
                                    <div class="result-detail" id="totalJuros">R$ 0,00</div>
                                    <small>Juros Acumulados</small>
                                </div>
                            </div>
                        </div>

                        <div id="placeholderInfo" class="text-center p-5">
                            <i class="bi bi-info-circle" style="font-size: 4rem; color: var(--cor-primaria);"></i>
                            <p class="mt-3 text-secondary">Preencha os campos ao lado e clique em "Calcular" para ver o
                                resultado da sua simulação.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class="bg-dark text-white py-4 mt-auto">
        <div class="container text-center">
            <p class="mb-0">
                &copy; <?php echo date('Y'); ?> SGEF - Sistema de Gestão e Educação Financeira. Todos os
                direitos reservados.
            </p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Função para formatar valor como moeda brasileira
        function formatarMoedaInput(valor) {
            // Remove tudo que não é número
            valor = valor.replace(/\D/g, '');

            // Converte para número e divide por 100 para ter centavos
            valor = (parseInt(valor) / 100).toFixed(2);

            // Formata com separadores
            valor = valor.replace('.', ',');
            valor = valor.replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.');

            return valor;
        }

        // Função para converter moeda formatada para número
        function moedaParaNumero(valor) {
            if (!valor) return 0;
            // Remove pontos de milhar e substitui vírgula por ponto
            return parseFloat(valor.replace(/\./g, '').replace(',', '.')) || 0;
        }

        // Adiciona formatação automática aos campos de moeda
        document.querySelectorAll('.currency-input').forEach(input => {
            input.addEventListener('input', function (e) {
                let valor = e.target.value;
                e.target.value = formatarMoedaInput(valor);
            });

            input.addEventListener('keypress', function (e) {
                if (e.key === 'Enter') {
                    calcularJurosCompostos();
                }
            });
        });

        // Permitir cálculo ao pressionar Enter nos outros inputs
        document.querySelectorAll('input:not(.currency-input)').forEach(input => {
            input.addEventListener('keypress', function (e) {
                if (e.key === 'Enter') {
                    calcularJurosCompostos();
                }
            });
        });

        function calcularJurosCompostos() {
            // Obter valores dos inputs
            const valorInicial = moedaParaNumero(document.getElementById('valorInicial').value);
            const aporteMensal = moedaParaNumero(document.getElementById('aporteMensal').value);
            const taxaJurosAnual = parseFloat(document.getElementById('taxaJuros').value) / 100 || 0;
            const periodoAnos = parseFloat(document.getElementById('periodo').value) || 0;

            // Validação
            if (periodoAnos <= 0) {
                alert('Por favor, insira um período válido.');
                return;
            }

            // Converter taxa anual para mensal jm =[(1+ja)^1/12]-1
            const taxaMensal = Math.pow(1 + taxaJurosAnual, 1 / 12) - 1;
            const periodoMeses = periodoAnos * 12;

            // Calcular montante final com juros compostos
            // Fórmula: M = C(1+i)^t + PMT * [((1+i)^t - 1) / i]
            let valorFinal = valorInicial * Math.pow(1 + taxaMensal, periodoMeses);

            if (aporteMensal > 0 && taxaMensal > 0) {
                valorFinal += aporteMensal * ((Math.pow(1 + taxaMensal, periodoMeses) - 1) / taxaMensal);
            } else if (aporteMensal > 0) {
                valorFinal += aporteMensal * periodoMeses;
            }

            // Calcular total investido
            const totalInvestido = valorInicial + (aporteMensal * periodoMeses);

            // Calcular juros acumulados
            const totalJuros = valorFinal - totalInvestido;

            // Exibir resultados
            document.getElementById('valorFinal').textContent = formatarMoeda(valorFinal);
            document.getElementById('totalInvestido').textContent = formatarMoeda(totalInvestido);
            document.getElementById('totalJuros').textContent = formatarMoeda(totalJuros);

            // Mostrar resultado e esconder placeholder
            document.getElementById('resultadoCalculadora').style.display = 'block';
            document.getElementById('placeholderInfo').style.display = 'none';
        }

        function formatarMoeda(valor) {
            return valor.toLocaleString('pt-BR', {
                style: 'currency',
                currency: 'BRL',
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });
        }
    </script>

</body>

</html>