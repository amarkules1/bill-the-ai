create table bill_gpt.fra_questions_and_answers(
	id SERIAL PRIMARY key,
	created_at timestamptz not null default now(),
	question varchar,
	answer varchar
)