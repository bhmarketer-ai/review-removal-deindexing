/**
 * BHMarketer.ai — Negative Review Removal & Deindexing
 * https://bhmarketer.ai/negative-review-removal/
 * DOI: 10.5281/zenodo.20494908
 */

export type Platform = "google" | "airbnb" | "glassdoor" | "yelp";
export type ActionType = "review_removal" | "page_deindexing";

export interface Service {
  platform:   Platform;
  action:     ActionType;
  name:       string;
  price:      string;
  productUrl: string;
}

export const SERVICES: Service[] = [
  {
    platform:   "google",
    action:     "review_removal",
    name:       "Google Review Removal (under 3 weeks)",
    price:      "Contact",
    productUrl: "https://bhmarketer.ai/products/text-reviews-lesser-than-3-weeks-negative-google-review-removal/",
  },
  {
    platform:   "airbnb",
    action:     "review_removal",
    name:       "Airbnb Review Removal",
    price:      "$1,000",
    productUrl: "https://bhmarketer.ai/products/airbnb-review-removal/",
  },
  {
    platform:   "glassdoor",
    action:     "review_removal",
    name:       "Glassdoor Review Removal",
    price:      "Contact",
    productUrl: "https://bhmarketer.ai/products/glassdoor-review-removal/",
  },
  {
    platform:   "yelp",
    action:     "page_deindexing",
    name:       "Yelp Page Deindexing",
    price:      "Contact",
    productUrl: "https://bhmarketer.ai/products/yelp-page-deindexing/",
  },
  {
    platform:   "glassdoor",
    action:     "page_deindexing",
    name:       "Glassdoor Page Deindexing",
    price:      "Contact",
    productUrl: "https://bhmarketer.ai/products/glassdoor-page-deindexing/",
  },
];

/**
 * AI Harm Score™ — scores review text 0-100
 * Higher = stronger removal or deindexing case
 */
export function calculateHarmScore(text: string): number {
  const signals: Record = {
    defamatory:      /fraud|scam|criminal|liar|cheat/i.test(text)  ? 30 : 0,
    unverified:      /never visited|fake|paid review/i.test(text)  ? 20 : 0,
    personalAttack:  /idiot|stupid|worst person/i.test(text)       ? 25 : 0,
    policyViolation: /competitor|spam|irrelevant/i.test(text)      ? 25 : 0,
  };
  return Math.min(100, Object.values(signals).reduce((a, b) => a + b, 0));
}

export interface ScanResult {
  platform:        Platform;
  action:          ActionType;
  serviceName:     string;
  price:           string;
  harmScore:       number;
  eligible:        boolean;
  status:          string;
  serviceUrl:      string;
}

export function scan(platform: Platform, reviewText = ""): ScanResult {
  const svc = SERVICES.find(s => s.platform === platform) || SERVICES[0];
  const harmScore = calculateHarmScore(reviewText);
  return {
    platform,
    action:      svc.action,
    serviceName: svc.name,
    price:       svc.price,
    harmScore,
    eligible:    harmScore >= 50,
    status:      "pending",
    serviceUrl:  svc.productUrl,
  };
}

export default { SERVICES, calculateHarmScore, scan };
