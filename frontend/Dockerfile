# ---- Phase 1: Build stage ----
FROM node:18-alpine AS builder

WORKDIR /fe

COPY package.json /fe/package.json

RUN npm install

COPY ./tsconfig.json /fe/tsconfig.json
COPY ./src /fe/src
COPY ./app /fe/app

RUN npm run build

# ---- Phase 2: Run stage ----
FROM node:18-alpine AS runner

WORKDIR /fe

COPY --from=builder /fe/package.json ./
COPY --from=builder /fe/node_modules ./node_modules
COPY --from=builder /fe/.next ./.next
# COPY --from=builder /fe/public ./public

ENV NODE_ENV=production
ENV PORT=3000

EXPOSE 3000

CMD ["npm", "run", "start"]
