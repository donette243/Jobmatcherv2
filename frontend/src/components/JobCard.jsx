import {
  ArrowUpRight,
  BriefcaseBusiness,
  Building2,
  MapPin,
} from "lucide-react";

function JobCard({ job }) {
  const title =
    job?.title ||
    job?.name ||
    "Вакансия без названия";

  const company =
    job?.company ||
    job?.company_name ||
    "Компания не указана";

  const location =
    job?.location ||
    job?.city ||
    "Местоположение не указано";

  const description =
    job?.description ||
    "Описание вакансии отсутствует.";

  const url =
    job?.url ||
    job?.link ||
    job?.apply_url ||
    null;

  const score =
    job?.match_score ??
    job?.score ??
    null;

  return (
    <article className="job-card">
      <div className="job-card-top">
        <div className="job-company-icon">
          <BriefcaseBusiness size={23} />
        </div>

        {score !== null && (
          <div className="job-match-score">
            {Math.round(Number(score))}%
            <span>совпадение</span>
          </div>
        )}
      </div>

      <div className="job-card-content">
        <h2>{title}</h2>

        <div className="job-meta">
          <span>
            <Building2 size={16} />
            {company}
          </span>

          <span>
            <MapPin size={16} />
            {location}
          </span>
        </div>

        <p>
          {description.length > 180
            ? `${description.slice(0, 180)}...`
            : description}
        </p>
      </div>

      <div className="job-card-footer">
        {url ? (
          <a
            href={url}
            target="_blank"
            rel="noopener noreferrer"
            className="job-link"
          >
            Подробнее
            <ArrowUpRight size={17} />
          </a>
        ) : (
          <span className="job-link disabled">
            Демонстрационная вакансия
          </span>
        )}
      </div>
    </article>
  );
}

export default JobCard;