import { Link } from "react-router-dom";
import {
  ArrowRight,
  BriefcaseBusiness,
  CheckCircle2,
  FileSearch,
  Search,
  Target,
} from "lucide-react";

function Home() {
  const token = localStorage.getItem("token");

  return (
    <main className="home-page">
      <section className="hero-section">
        <div className="hero-content">
          <div className="hero-badge">
            <Search size={16} />
            <span>Умный поиск работы</span>
          </div>

          <h1>
            Найдите вакансии, которые{" "}
            <span>действительно подходят</span> вашему профилю.
          </h1>

          <p>
            JobMatcher анализирует ваш профиль и навыки, чтобы помочь вам
            найти наиболее подходящие профессиональные возможности
          </p>

          <div className="hero-actions">
            {token ? (
              <Link to="/dashboard" className="primary-button">
                Перейти в панель управления
                <ArrowRight size={18} />
              </Link>
            ) : (
              <>
                <Link to="/register" className="primary-button">
                  Начать бесплатно
                  <ArrowRight size={18} />
                </Link>

                <Link to="/login" className="secondary-button">
                  Войти
                </Link>
              </>
            )}
          </div>

          <div className="hero-trust">
            <span>
              <CheckCircle2 size={17} />
              Анализ резюме
            </span>

            <span>
              <CheckCircle2 size={17} />
              Сопоставление навыков
            </span>

            <span>
              <CheckCircle2 size={17} />
              Рекомендации
            </span>
          </div>
        </div>

        <div className="hero-visual">
          <div className="floating-card card-one">
            <div className="floating-icon">
              <FileSearch size={20} />
            </div>

            <div>
              <strong>Резюме проанализировано</strong>
              <span>Навыки определены</span>
            </div>
          </div>

          <div className="matching-card">
            <div className="matching-card-top">
              <div className="matching-icon">
                <Target size={24} />
              </div>

              <span>Соответствие вакансии</span>
            </div>

            <div className="match-score">
              <strong>92%</strong>
              <span>Отличное соответствие</span>
            </div>

            <div className="score-bar">
              <div className="score-progress" />
            </div>

            <div className="matching-skills">
              <span>Python</span>
              <span>FastAPI</span>
              <span>SQL</span>
              <span>Docker</span>
            </div>
          </div>

          <div className="floating-card card-two">
            <div className="floating-icon">
              <BriefcaseBusiness size={20} />
            </div>

            <div>
              <strong>Новая вакансия</strong>
              <span>Подходит вашему профилю</span>
            </div>
          </div>
        </div>
      </section>

      <section className="features-section">
        <div className="section-heading">
          <span>КАК ЭТО РАБОТАЕТ</span>

          <h2>Более эффективный поиск работы</h2>

          <p>
            JobMatcher сопровождает вас от анализа профиля до поиска вакансий,
            которые лучше всего соответствуют вашим навыкам.
          </p>
        </div>

        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-number">01</div>

            <div className="feature-icon">
              <FileSearch size={24} />
            </div>

            <h3>Загрузите резюме</h3>

            <p>
              Загрузите своё резюме, и JobMatcher определит ваши навыки и
              профессиональный профиль.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-number">02</div>

            <div className="feature-icon">
              <Target size={24} />
            </div>

            <h3>Оцените соответствие</h3>

            <p>
              Сравните свой профиль с навыками и требованиями, указанными в
              различных вакансиях.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-number">03</div>

            <div className="feature-icon">
              <BriefcaseBusiness size={24} />
            </div>

            <h3>Найдите подходящие вакансии</h3>

            <p>
              Получайте рекомендации на основе вашего профессионального
              профиля, навыков и предпочтений.
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}

export default Home;

