import { useEffect, useState } from "react";
import { Search, BriefcaseBusiness, LoaderCircle } from "lucide-react";
import JobCard from "../components/JobCard";
import { getJobs } from "../services/api";

function Jobs() {
  const [jobs, setJobs] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadJobs = async () => {
      try {
        const data = await getJobs();

        if (Array.isArray(data)) {
          setJobs(data);
        } else {
          setJobs(data?.jobs || []);
        }
      } catch (err) {
        setError(
          err.message || "Не удалось загрузить вакансии."
        );
      } finally {
        setLoading(false);
      }
    };

    loadJobs();
  }, []);

  const filteredJobs = jobs.filter((job) => {
    const query = search.toLowerCase().trim();

    if (!query) {
      return true;
    }

    const title = job?.title?.toLowerCase() || "";
    const company = job?.company?.toLowerCase() || "";
    const description = job?.description?.toLowerCase() || "";

    return (
      title.includes(query) ||
      company.includes(query) ||
      description.includes(query)
    );
  });

  return (
    <main className="jobs-page">
      <div className="page-container">
        <section className="page-header">
          <div>
            <span className="page-eyebrow">
              <BriefcaseBusiness size={16} />
              Возможности
            </span>

            <h1>Вакансии</h1>

            <p>
              Просматривайте доступные возможности и находите
              вакансии, которые соответствуют вашему профилю.
            </p>
          </div>
        </section>

        <section className="jobs-search">
          <Search size={20} />

          <input
            type="text"
            placeholder="Поиск вакансии или компании..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />
        </section>

        {loading && (
          <div className="loading-state">
            <LoaderCircle
              className="loading-spinner"
              size={30}
            />

            <p>Загрузка вакансий...</p>
          </div>
        )}

        {!loading && error && (
          <div className="empty-state error-state">
            <BriefcaseBusiness size={40} />

            <h2>Не удалось загрузить вакансии</h2>

            <p>{error}</p>
          </div>
        )}

        {!loading && !error && filteredJobs.length === 0 && (
          <div className="empty-state">
            <BriefcaseBusiness size={40} />

            <h2>Вакансии не найдены</h2>

            <p>
              {search
                ? "Попробуйте изменить поисковый запрос."
                : "В данный момент доступных вакансий нет."}
            </p>
          </div>
        )}

        {!loading && !error && filteredJobs.length > 0 && (
          <section className="jobs-grid">
            {filteredJobs.map((job, index) => (
              <JobCard
                key={job?.id || job?.job_id || index}
                job={job}
              />
            ))}
          </section>
        )}
      </div>
    </main>
  );
}

export default Jobs;

