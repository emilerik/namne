const httpProtocol = import.meta.env.VITE_PUBLIC_API_HTTP_PROTOCOL || "";
const baseHost = import.meta.env.VITE_PUBLIC_API_URL || "";
export const API_URL = `${httpProtocol}${baseHost}`;
