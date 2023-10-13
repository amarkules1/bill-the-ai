create table bill_likes (
    bill_id UUID not null,
    user_id UUID not null,
    created_at timestamptz not null default now(),
    PRIMARY key (bill_id, user_id)
);