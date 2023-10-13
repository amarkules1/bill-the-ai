create table question_likes (
    question_id UUID not null,
    bill_id UUID not null,
    user_id UUID not null,
    created_at timestamptz not null default now(),
    PRIMARY key (question_id, user_id)
);