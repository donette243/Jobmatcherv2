import { useEffect, useState } from "react";
import {
  LoaderCircle,
  Sparkles,
  Target,
} from "lucide-react";
import JobCard from "../components/JobCard";
import { getRecommendations } from "../services/api";

function Recommendations() {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadRecommendations = async () => {
      try {
        const data = await getRecommendations();

        if (Array.isArray(data)) {
          setRecommendations(data);
        } else {
          setRecommendations(
            data?.recommendations ||
              data?.jobs ||
              []
          );
        }
      } catch (err) {
        setError(
          err.message ||
            "Не удалось загрузить рекомендации"
        );
      } finally {
        setLoading(false);
      }
    };

    loadRecommendations();
  }, []);

  return (
    <main className="recommendations-page">
      <div className="page-container">
        <section className="page-header">
          <div>
            <span className="page-eyebrow">
              <Sparkles size={16} />
              Персональный подбор вакансий
            </span>

            <h1>Мои рекомендации</h1>

            <p>
              Найдите вакансии, которые лучше всего соответствуют
              вашему профилю и навыкам
            </p>
          </div>
        </section>

        <section className="recommendation-banner">
          <div className="recommendation-banner-icon">
            <Target size={25} />
          </div>

          <div>
            <h2>Лучшие возможности для вас</h2>

            <p>
              Вакансии отсортированы по степени соответствия
              вашему профилю
            </p>
          </div>
        </section>

        {loading && (
          <div className="loading-state">
            <LoaderCircle
              className="loading-spinner"
              size={30}
            />

            <p>
              Анализ вашего профиля...
            </p>
          </div>
        )}

        {!loading && error && (
          <div className="empty-state error-state">
            <Target size={40} />

            <h2>
              Не удалось загрузить рекомендации
            </h2>

            <p>{error}</p>
          </div>
        )}

        {!loading &&
          !error &&
          recommendations.length === 0 && (
            <div className="empty-state">
              <Sparkles size={40} />

              <h2>
                Пока нет рекомендаций
              </h2>

              <p>
                Добавьте своё резюме и заполните профиль,
                чтобы получать персональные рекомендации
              </p>
            </div>
          )}

        {!loading &&
          !error &&
          recommendations.length > 0 && (
            <section className="jobs-grid">
              {recommendations.map((job, index) => (
                <JobCard
                  key={
                    job?.id ||
                    job?.job_id ||
                    index
                  }
                  job={job}
                />
              ))}
            </section>
          )}
      </div>
    </main>
  );
}

export default Recommendations;

