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
    "Poste sans titre";

  const company =
    job?.company ||
    job?.company_name ||
    "Entreprise";

  const location =
    job?.location ||
    job?.city ||
    "Localisation non précisée";

  const description =
    job?.description ||
    "Aucune description disponible.";

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
            <span>match</span>
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
            ? '${description.slice(0, 180)}...'
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
            Voir l'offre
            <ArrowUpRight size={17} />
          </a>
        ) : (
          <span className="job-link disabled">
            Détails indisponibles
          </span>
        )}
      </div>
    </article>
  );
}

export default JobCard;