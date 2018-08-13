package no.uio.ifi.pascal2100.parser;

import java.util.ArrayList;

import no.uio.ifi.pascal2100.scanner.Scanner;

public abstract class Type extends PascalSyntax {

	public TypeDecl tdecl;
	public ArrayType art;
	public VarDecl vadecl;
	public ArrayList<TypeName> tnam= new ArrayList<TypeName>();
	public static Type tp = null;

	public Type(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		
	}
	
	/**
     * Parse a Type.
     * @param Scanner Tokens.
     * @return the Type object of the parse tree.
     * Range,leftpar ,array ,name token parsing
     */

	public static Type parse(Scanner s) {
		// TODO Auto-generated method stub
		enterParser("type");
		
		switch (s.nextToken.kind) {
		case rangeToken:
			tp=RangeType.parse(s);
			break;
		
		default:
		 break;}
		switch (s.curToken.kind ) {
		case leftParToken:
			
		tp = EnumType.parse(s); break;
		case arrayToken:
		tp = ArrayType.parse(s); break;
		
		case nameToken:
			tp = TypeName.parse(s);
		
		default:
		 break;
		}
		leaveParser("type");
		return tp;
	}

	}

