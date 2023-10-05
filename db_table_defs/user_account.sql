create table bill_gpt.user_account(
	user_id UUID PRIMARY key,
	user_name varchar not null,
	email varchar not null,
	password varchar not null,
	created_at timestamptz not null default now(),
	updated_at timestamptz not null default now(),
	feature_emails bool default true,
	email_verified bool default false,
	email_verification_token UUID not null default gen_random_uuid(),
	session_token UUID,
	session_token_expires_at timestamptz,
	password_reset_token UUID,
	password_reset_token_expires_at timestamptz
);