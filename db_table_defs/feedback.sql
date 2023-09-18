create table bill_gpt.app_feedback(
	id SERIAL PRIMARY key,
	created_at timestamptz not null default now(),
	feedback varchar,
	email varchar
)