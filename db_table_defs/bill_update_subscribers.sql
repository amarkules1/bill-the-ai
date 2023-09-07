create table bill_gpt.bill_update_subscribers(
	id SERIAL PRIMARY key,
	created_at timestamptz not null default now(),
	name varchar,
	email varchar,
	is_active bool default true,
	unsubscribe_dt timestamptz,
	verification_id uuid
)