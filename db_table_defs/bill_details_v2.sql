create table bill_gpt.bill_details_v2(
    bill_id UUID PRIMARY key,
    bill_title varchar,
    bill_alias varchar,
    summary varchar,
    wiki_link varchar,
    full_text_link varchar,
    created_at timestamptz not null default now()
);