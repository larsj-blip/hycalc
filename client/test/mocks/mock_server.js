import {setupServer} from "msw/node";
import {handler} from "./handler.js";

export const server = setupServer(handler)