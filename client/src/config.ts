const baseHost = import.meta.env.VITE_PUBLIC_API_URL || "";
const httpProtocol = import.meta.env.VITE_PUBLIC_API_HTTP_PROTOCOL || "";
export const API_URL = `${httpProtocol}${baseHost}`;
