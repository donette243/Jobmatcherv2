import { Link } from "react-router-dom";
import {
  ArrowRight,
  BriefcaseBusiness,
  FileText,
  Search,
  Target,
  UserRound,
} from "lucide-react";

function Dashboard() {
  return (
    <main className="dashboard-page">
      <div className="page-container">
        <section className="dashboard-welcome">
          <div>
            <span className="dashboard-eyebrow">
              <UserRound size={16} />
              Личный кабинет
            </span>

            <h1>Добро пожаловать в JobMatcher</h1>

            <p>
              Управляйте своим профилем, анализируйте резюме и находите
              вакансии, которые лучше всего соответствуют вашим навыкам
            </p>
          </div>

          <Link to="/jobs" className="primary-button">
            Смотреть вакансии
            <ArrowRight size={18} />
          </Link>
        </section>

        <section className="dashboard-grid">
          <Link to="/profile" className="dashboard-card">
            <div className="dashboard-card-icon">
              <UserRound size={24} />
            </div>

            <div>
              <h2>Мой профиль</h2>
              <p>
                Просматривайте и заполняйте информацию о своём
                профессиональном профиле.
              </p>
            </div>

            <ArrowRight className="dashboard-arrow" size={20} />
          </Link>

          <Link to="/cv" className="dashboard-card">
            <div className="dashboard-card-icon">
              <FileText size={24} />
            </div>

            <div>
              <h2>Моё резюме</h2>
              <p>
                Загрузите резюме, чтобы JobMatcher мог проанализировать
                ваши навыки
              </p>
            </div>

            <ArrowRight className="dashboard-arrow" size={20} />
          </Link>

          <Link to="/jobs" className="dashboard-card">
            <div className="dashboard-card-icon">
              <Search size={24} />
            </div>

            <div>
              <h2>Вакансии</h2>
              <p>
                Просматривайте доступные вакансии и находите подходящие
                профессиональные возможности.
              </p>
            </div>

            <ArrowRight className="dashboard-arrow" size={20} />
          </Link>

          <Link to="/recommendations" className="dashboard-card">
            <div className="dashboard-card-icon">
              <BriefcaseBusiness size={24} />
            </div>

            <div>
              <h2>Рекомендации</h2>
              <p>
                Просматривайте вакансии с наиболее высоким показателем
                соответствия вашему профилю.
              </p>
            </div>

            <ArrowRight className="dashboard-arrow" size={20} />
          </Link>
        </section>

        <section className="dashboard-banner">
          <div className="dashboard-banner-icon">
            <Target size={25} />
          </div>

          <div>
            <h2>Улучшите результаты поиска</h2>
            <p>
              Добавьте резюме и укажите свои профессиональные предпочтения,
              чтобы получать более точные рекомендации.
            </p>
          </div>

          <Link to="/cv" className="secondary-button">
            Добавить резюме
          </Link>
        </section>
      </div>
    </main>
  );
}

export default Dashboard;

